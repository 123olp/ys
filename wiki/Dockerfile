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

FROM alpine:3.22 AS universal-language-selector

ARG ULS_COMMIT=87068f1dc722fbff17346f069a73539737267cc4
ARG ULS_SHA256=564e4836f4e164e7a3b7c70d0ce513aa55801089455959eb2da344574e2dd914

RUN apk add --no-cache ca-certificates tar wget \
    && wget -qO /tmp/uls.tar.gz \
       "https://github.com/wikimedia/mediawiki-extensions-UniversalLanguageSelector/archive/${ULS_COMMIT}.tar.gz" \
    && echo "${ULS_SHA256}  /tmp/uls.tar.gz" | sha256sum -c - \
    && mkdir -p /out/UniversalLanguageSelector \
    && tar -xzf /tmp/uls.tar.gz \
       -C /out/UniversalLanguageSelector \
       --strip-components=1

FROM mediawiki:1.46.0

COPY --from=pageforms /out/PageForms /var/www/html/extensions/PageForms
COPY --from=universal-language-selector /out/UniversalLanguageSelector /var/www/html/extensions/UniversalLanguageSelector
COPY docker/entrypoint.sh /usr/local/bin/human-infra-wiki-entrypoint

RUN chmod 0755 /usr/local/bin/human-infra-wiki-entrypoint

ENTRYPOINT ["human-infra-wiki-entrypoint"]
CMD ["apache2-foreground"]
