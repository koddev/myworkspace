FROM openjdk:8-jre

ENV CEREBRO_VERSION 0.9.4
RUN cd /opt/ \
    && wget -O cerebro-${CEREBRO_VERSION}.tgz https://github.com/lmenezes/cerebro/releases/download/v${CEREBRO_VERSION}/cerebro-${CEREBRO_VERSION}.tgz \
    && tar zxvf cerebro-${CEREBRO_VERSION}.tgz \
    && rm cerebro-${CEREBRO_VERSION}.tgz \
    && mkdir cerebro-${CEREBRO_VERSION}/logs \
    && mv cerebro-${CEREBRO_VERSION} cerebro 
     

WORKDIR /opt/cerebro

RUN rm ./conf/application.conf
COPY application.conf ./conf/application.conf

EXPOSE 9000
CMD ["./bin/cerebro"]