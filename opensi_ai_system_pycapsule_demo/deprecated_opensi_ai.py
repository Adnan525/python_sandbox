import sys
sys.path.append("/home/s448780/workspace/sandbox/") # this is to point to the root directory

# from llm_agent.llm import LLM
from llm_agent.ollama import Ollama_server
from sandbox_service.sandbox import Sandbox
from sandbox_service.container import Container
from util import create_py_file, create_requirements_file, clean

# llm_agent = LLM("codellama")
llm_agent = Ollama_server("mistral")
sandbox = Sandbox()
container = Container()

code_to_run = llm_agent.request_code("Write a python code to multipy 2 matrices")
print(f"[INFO] Raw response - \n{code_to_run}")

# parsing
# regex --old
# libraries = parse_library_names(code_to_run)
# print(f"[INFO] Libraies being used - {libraries}")
requirements, code, example = llm_agent.parse_input(code_to_run)
print(f"[INFO] Code -\n{code}")
print(f"[INFO] Example -\n{example}")
print(f"[INFO] Requirements - {requirements}")

# creating python file
create_py_file("opensi_ai_system/main", code + "\n" + example)

# creating requirements file
is_run_pip_required = create_requirements_file(requirements)
# if is_run_pip_required:
#     install_requirements() # this will attempt to install the requirements in the local machine

# creating container
return_code = -1
if not container.check_if_container_exists():
    return_code = container.create_container()
else:
    return_code = container.start_container()

# delete the file from local volume
clean(["main.py", "requirements.txt"])
# clean()
