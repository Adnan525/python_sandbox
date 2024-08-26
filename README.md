# OpenSI PyCapsule Service

Pull the docker image. It's based on ubuntu 20.04 and installs python3 by default, does not install any other libraries.
```
docker pull ghost525/sandbox_python
```

The Container class will mount the ```/opensi_ai_system``` to the container's workdir which is set to ```/usr/src/app```.
The following command is executed when the image is found - 
```
docker run --name opensi_sandbox_service -v __use_correct_path__/workspace/sandbox/opensi_ai_system:/usr/src/app sandbox_python 
# do not change the container name
```

Run ```opensi_ai_system_pycapsule_demo/ollama_opensi.py``` which will request user input and will start Ollama server with Mistral 7B by default.  
Container will return any error along with ```exist code = 0|1```. If  exit code is 1, the pycapsule loop gets activated which will do the following -  
- Keep track of the conversation history (only 1 pair for code generation)
- Keep track of the original question
- Generate context based on origin_question and conversation history
- Communicate with the LLM with the context, origin_question and error from PyCapsule
- The loop will break only if the updated code from LLM compiles with <b>exit code 0</b>  
  
![Py-capsule](https://github.com/Adnan525/python_sandbox/blob/master/pycapsule.png)


# Important
- Everytime we use the ollama-server, the code will start a new process, run the query and close the process.  
- The code parsing can break if model starts to respond in plain English, at the moment prompt engineering has been employed to force the model to generate response that is compatible with <b>Python Compiler</b>. This approach while effective for general use, does not always work when an error is detected in the generated code by the LLM. 

# Requirements
- Ollama on the host machine  
[Ollama Download](https://ollama.com/download)
```
curl -fsSL https://ollama.com/install.sh | sh 
```
- Docker on the host machine  
[Docker](https://docs.docker.com/engine/install/ubuntu/)

# Known Issues
- Paths for container mount and clean needs to be dynamically inserted or use parseargs to request user input
- subprocess.Popen can keep a process alive but communincation with the shell becomes too complicated, refer to ```llm_agent/test``` files
- The code parsing from mistral response is quite primitive
