# we can try to replace this with alpine
FROM ubuntu:20.04
# use default answer for all prompts
ENV DEBIAN_FRONTEND=noninteractive

# python, removing all cached files to reduce the image size
RUN apt update && \
    apt install -y python3 python3-pip && \
    apt clean && \ 
    rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

# entry point to bash
# ENTRYPOINT ["/bin/bash"]

# shell script for checking
RUN echo '#!/bin/sh\n\
if [ -f /usr/src/app/main.py ]; then\n\
    echo "Executing main.py..."\n\
    python3 /usr/src/app/main.py\n\
else\n\
    echo "Nothing to execute, shutting down."\n\
fi' > /usr/src/app/start.sh

# run the shell script
# CMD ["chmod +x /usr/src/app/start.sh"]
ENTRYPOINT ["/usr/src/app/start.sh"]
