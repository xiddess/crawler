import requests
from bs4 import BeautifulSoup
import sqlite3
from urllib.robotparser import RobotFileParser
from urllib.parse import urlparse
import time
import logging

# Konfigurasi logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Inisialisasi database
def init_db():
    conn = sqlite3.connect('crawler.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS pages
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  url TEXT UNIQUE,
                  content TEXT,
                  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    return conn

# Cek robots.txt
def can_fetch(url):
    try:
        parsed_url = urlparse(url)
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
        robots_url = f"{base_url}/robots.txt"
        rp = RobotFileParser()
        rp.set_url(robots_url)
        rp.read()
        return rp.can_fetch("*", url)
    except Exception as e:
        logging.warning(f"Error checking robots.txt for {url}: {e}")
        return True  # Default allow jika robots.txt tidak bisa diakses

# Fungsi untuk crawl halaman
def crawl(url, conn):
    if not can_fetch(url):
        logging.info(f"Skipping {url} (disallowed by robots.txt)")
        return

    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            content = soup.prettify()

            # Simpan ke database
            c = conn.cursor()
            c.execute("INSERT OR IGNORE INTO pages (url, content) VALUES (?, ?)", (url, content))
            conn.commit()
            logging.info(f"Crawled: {url}")

            # Ekstrak semua link dari halaman
            for link in soup.find_all('a', href=True):
                next_url = link['href']
                if next_url.startswith('http'):
                    crawl(next_url, conn)  # Rekursif untuk crawl link yang ditemukan
    except Exception as e:
        logging.error(f"Error crawling {url}: {e}")

# Fungsi utama
def main():
    conn = init_db()
    start_url = input("Masukkan Url: ")  # URL awal, contoh http://example.com
    crawl(start_url, conn)
    conn.close()

if __name__ == "__main__":
    main()