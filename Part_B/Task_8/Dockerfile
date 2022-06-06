#a. Start FROM a base image.  Version of Python to be used can be passed in as a parameter at build time.

#ARG version= 3.8
FROM python:3.8
#FROM python:${version}

#c. Change to app directory

WORKDIR /Part_A/Backend

#d. COPY files into the above directory

COPY ./*.py ./
COPY requirements.txt ./requirements.txt


#b. Update package manager and install required packages

RUN pip install --upgrade --no-cache-dir -r ./requirements.txt

#e. Set environment variable. This assigns a confirmation message 
#   of "Query Successful" to the variable Confirmation. This can
#   be reconfigured outside of the container.

ENV Confirmation="Query Successful"


#i. Use VOLUME to allow the container to save data

VOLUME /database_volume

#f. Use ENTRYPOINT to run a default command

ENTRYPOINT ["uvicorn", "main:app"] 

#g. Use CMD to run another default command.  A CMD command can be overridden, whereas an ENTRYPOINT command cannot. 
#   The port number can therefore be overidden when a user executes the "docker run" command + a parameter.

CMD ["--host", "0.0.0.0", "--port", "64308"]

#h. Use EXPOSE to document the port the container exposes

EXPOSE 80


#j.  How to to build the Dockerfile. In the command line. cd to working directory. Build with: docker build -t jdock007/sakila_app_1.0 .



#k.  How to run the resulting Docker image. Use: docker run -i sakila_app_1.0



#l. DockerHub Location: https://hub.docker.com/repository/docker/jdock007/sakila_app_1.0
