FROM alpine:3.22 AS pageforms

ARG PAGE_FORMS_VERSION=6.0.9
ARG PAGE_FORMS_SHA256=d4c4966169bde055b974eda3d9b79997d08f4a00514021631db6922ff09471cf

RUN apk add --no-cache ca-certificates tar wget \
    && wget -qO /tmp/pageforms.tar.gz \
       "https://github.com/wikimedia/mediawiki-extensions-PageForms/archive/refs/tags/${PAGE_FORMS_VERSION}.tar.gz" \
    && echo "${PAGE_FORMS_SHA256}  /tmp/pageforms.tar.gz" | sha256sum -c - \
    && mkdir -p /tmp/pageforms /out \
    && tar -xzf /tmp/pageforms.tar.gz -C /tmp/pageforms --strip-components=1 \
    && mv /tmp/pageforms /out/PageForms

FROM mediawiki:1.46.0

COPY --from=pageforms /out/PageForms /var/www/html/extensions/PageForms
COPY docker/entrypoint.sh /usr/local/bin/human-infra-wiki-entrypoint

RUN chmod 0755 /usr/local/bin/human-infra-wiki-entrypoint

ENTRYPOINT ["human-infra-wiki-entrypoint"]
CMD ["apache2-foreground"]
