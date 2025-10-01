FROM freeradius/freeradius-server:latest

# Install utils
RUN apt-get update && apt-get install -y \
    freeradius-mysql \
    && rm -rf /var/lib/apt/lists/*

# Copy konfigurasi tambahan jika perlu (opsional)
# COPY mods-available/sql /etc/freeradius/3.0/mods-available/sql

CMD ["freeradius", "-f"]
