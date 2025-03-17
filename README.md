# Website Crawler dengan PDF Downloader

Proyek ini adalah sebuah bot crawler website yang dapat mengekstrak konten dari halaman web dan mengunduh file PDF yang ditemukan selama proses crawling. Crawler ini dirancang untuk menghormati aturan `robots.txt` dan menyimpan hasil crawling ke dalam database SQLite.

## Fitur

- **Crawling Halaman Web**: Menjelajahi halaman web dan mengekstrak kontennya.
- **Download PDF**: Mengunduh file PDF yang ditemukan selama proses crawling.
- **Penyimpanan Database**: Menyimpan hasil crawling ke dalam database SQLite.
- **Respect `robots.txt`**: Menghormati aturan `robots.txt` dari website yang di-crawl.
- **Shell Script**: Memudahkan pengguna untuk menjalankan crawler tanpa mengetik perintah Python secara manual.

## Persyaratan

- Python 3.7 atau lebih baru
- Library Python: `requests`, `beautifulsoup4`, `lxml`

## Instalasi

1. **Clone Repository**:
   ```bash
   git clone https://github.com/username/crawler-project.git
   cd crawler-project
