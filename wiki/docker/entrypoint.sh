#!/bin/sh
set -eu

mkdir -p /config /var/www/html/images
chown -R www-data:www-data /var/www/html/images

if [ -f /config/LocalSettings.php ]; then
    cp /config/LocalSettings.php /var/www/html/LocalSettings.php
    chown www-data:www-data /var/www/html/LocalSettings.php
    chmod 0640 /var/www/html/LocalSettings.php
fi

exec docker-php-entrypoint "$@"
