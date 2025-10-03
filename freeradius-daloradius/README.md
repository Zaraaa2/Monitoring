# Panduan Instalasi FreeRADIUS + daloRADIUS (Docker)

## 1. Update & Upgrade Ubuntu

``` bash
sudo apt update -y
sudo apt upgrade -y
```

## 2. Masuk ke Mode Root

``` bash
sudo su
```

## 3. Install Docker Compose V2

Untuk menghindari error `Keyerror`, gunakan perintah berikut:

``` bash
snap install docker
```

## 4. Cek Versi Docker Compose

``` bash
docker compose version
```

Pastikan sudah keluar **Docker V2**.

## 5. Clone Repository dari GitHub

``` bash
git clone https://github.com/Zaraaa2/Monitoring.git
cd Monitoring/freeradius-daloradius
```

## 6. Build & Jalankan Container

Gunakan `docker-compose.yml` yang sudah tersedia:

``` bash
docker compose up -d --build
```

## 7. Cek Container Berjalan

``` bash
docker ps
```

Jika status container sudah **"Up"**, lanjut ke langkah berikut.

## 8. Akses daloRADIUS Web Management

Buka browser dan akses:

    http://IP-PUBLIC:8080

Login dengan kredensial default: - **Username:** `administrator`\
- **Password:** `radius`
PASTIKAN PORT 1812 & 1813/UDP TERBUKA UNTUK MENGHINDARI ERROR SAAT MASUK WEB