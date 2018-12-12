
(base) C:\>pip --version
pip 10.0.1 from C:\Users\User\Anaconda3\lib\site-packages\pip (python 3.7)


(base) C:\>pip install --upgrade pip
ERROR: To modify pip, please run the following command:
C:\Users\User\Anaconda3\python.exe -m pip install --upgrade pip
You are using pip version 10.0.1, however version 18.1 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.


(base) C:\>python -m pip install --upgrade pip
Collecting pip
  Downloading https://files.pythonhosted.org/packages/c2/d7/90f34cb0d83a6c5631cf
71dfe64cc1054598c843a92b400e55675cc2ac37/pip-18.1-py2.py3-none-any.whl (1.3MB)
    100% |¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦¦| 1.3MB 1.6MB/s
twisted 18.7.0 requires PyHamcrest>=1.9.0, which is not installed.
Installing collected packages: pip
  Found existing installation: pip 10.0.1
    Uninstalling pip-10.0.1:
      Successfully uninstalled pip-10.0.1
Successfully installed pip-18.1


(base) C:\>pip install jupyter
Requirement already satisfied: jupyter in c:\users\user\anaconda3\lib\site-packa
ges (1.0.0)
Requirement already satisfied: ipywidgets in c:\users\user\anaconda3\lib\site-pa
ckages (from jupyter) (7.4.1)
Requirement already satisfied: notebook in c:\users\user\anaconda3\lib\site-pack
ages (from jupyter) (5.6.0)
Requirement already satisfied: nbconvert in c:\users\user\anaconda3\lib\site-pac
kages (from jupyter) (5.4.0)
Requirement already satisfied: ipykernel in c:\users\user\anaconda3\lib\site-pac
kages (from jupyter) (4.10.0)
Requirement already satisfied: jupyter-console in c:\users\user\anaconda3\lib\si
te-packages (from jupyter) (5.2.0)
Requirement already satisfied: qtconsole in c:\users\user\anaconda3\lib\site-pac
kages (from jupyter) (4.4.1)
Requirement already satisfied: widgetsnbextension~=3.4.0 in c:\users\user\anacon
da3\lib\site-packages (from ipywidgets->jupyter) (3.4.1)
Requirement already satisfied: ipython>=4.0.0; python_version >= "3.3" in c:\use
rs\user\anaconda3\lib\site-packages (from ipywidgets->jupyter) (6.5.0)
Requirement already satisfied: nbformat>=4.2.0 in c:\users\user\anaconda3\lib\si
te-packages (from ipywidgets->jupyter) (4.4.0)
Requirement already satisfied: traitlets>=4.3.1 in c:\users\user\anaconda3\lib\s
ite-packages (from ipywidgets->jupyter) (4.3.2)
Requirement already satisfied: ipython-genutils in c:\users\user\anaconda3\lib\s
ite-packages (from notebook->jupyter) (0.2.0)
Requirement already satisfied: tornado>=4 in c:\users\user\anaconda3\lib\site-pa
ckages (from notebook->jupyter) (5.1)
Requirement already satisfied: prometheus-client in c:\users\user\anaconda3\lib\
site-packages (from notebook->jupyter) (0.3.1)
Requirement already satisfied: jupyter-client>=5.2.0 in c:\users\user\anaconda3\
lib\site-packages (from notebook->jupyter) (5.2.3)
Requirement already satisfied: jupyter-core>=4.4.0 in c:\users\user\anaconda3\li
b\site-packages (from notebook->jupyter) (4.4.0)
Requirement already satisfied: pyzmq>=17 in c:\users\user\anaconda3\lib\site-pac
kages (from notebook->jupyter) (17.1.2)
Requirement already satisfied: jinja2 in c:\users\user\anaconda3\lib\site-packag
es (from notebook->jupyter) (2.10)
Requirement already satisfied: terminado>=0.8.1 in c:\users\user\anaconda3\lib\s
ite-packages (from notebook->jupyter) (0.8.1)
Requirement already satisfied: Send2Trash in c:\users\user\anaconda3\lib\site-pa
ckages (from notebook->jupyter) (1.5.0)
Requirement already satisfied: mistune>=0.8.1 in c:\users\user\anaconda3\lib\sit
e-packages (from nbconvert->jupyter) (0.8.3)
Requirement already satisfied: pygments in c:\users\user\anaconda3\lib\site-pack
ages (from nbconvert->jupyter) (2.2.0)
Requirement already satisfied: entrypoints>=0.2.2 in c:\users\user\anaconda3\lib
\site-packages (from nbconvert->jupyter) (0.2.3)
Requirement already satisfied: bleach in c:\users\user\anaconda3\lib\site-packag
es (from nbconvert->jupyter) (2.1.4)
Requirement already satisfied: pandocfilters>=1.4.1 in c:\users\user\anaconda3\l
ib\site-packages (from nbconvert->jupyter) (1.4.2)
Requirement already satisfied: testpath in c:\users\user\anaconda3\lib\site-pack
ages (from nbconvert->jupyter) (0.3.1)
Requirement already satisfied: defusedxml in c:\users\user\anaconda3\lib\site-pa
ckages (from nbconvert->jupyter) (0.5.0)
Requirement already satisfied: prompt-toolkit<2.0.0,>=1.0.0 in c:\users\user\ana
conda3\lib\site-packages (from jupyter-console->jupyter) (1.0.15)
Requirement already satisfied: simplegeneric>0.8 in c:\users\user\anaconda3\lib\
site-packages (from ipython>=4.0.0; python_version >= "3.3"->ipywidgets->jupyter
) (0.8.1)
Requirement already satisfied: pickleshare in c:\users\user\anaconda3\lib\site-p
ackages (from ipython>=4.0.0; python_version >= "3.3"->ipywidgets->jupyter) (0.7
.4)
Requirement already satisfied: colorama; sys_platform == "win32" in c:\users\use
r\anaconda3\lib\site-packages (from ipython>=4.0.0; python_version >= "3.3"->ipy
widgets->jupyter) (0.3.9)
Requirement already satisfied: decorator in c:\users\user\anaconda3\lib\site-pac
kages (from ipython>=4.0.0; python_version >= "3.3"->ipywidgets->jupyter) (4.3.0
)
Requirement already satisfied: backcall in c:\users\user\anaconda3\lib\site-pack
ages (from ipython>=4.0.0; python_version >= "3.3"->ipywidgets->jupyter) (0.1.0)

Requirement already satisfied: setuptools>=18.5 in c:\users\user\anaconda3\lib\s
ite-packages (from ipython>=4.0.0; python_version >= "3.3"->ipywidgets->jupyter)
 (40.2.0)
Requirement already satisfied: jedi>=0.10 in c:\users\user\anaconda3\lib\site-pa
ckages (from ipython>=4.0.0; python_version >= "3.3"->ipywidgets->jupyter) (0.12
.1)
Requirement already satisfied: jsonschema!=2.5.0,>=2.4 in c:\users\user\anaconda
3\lib\site-packages (from nbformat>=4.2.0->ipywidgets->jupyter) (2.6.0)
Requirement already satisfied: six in c:\users\user\anaconda3\lib\site-packages
(from traitlets>=4.3.1->ipywidgets->jupyter) (1.11.0)
Requirement already satisfied: python-dateutil>=2.1 in c:\users\user\anaconda3\l
ib\site-packages (from jupyter-client>=5.2.0->notebook->jupyter) (2.7.3)
Requirement already satisfied: MarkupSafe>=0.23 in c:\users\user\anaconda3\lib\s


(base) C:\>jupyter notebook
[I 11:28:41.340 NotebookApp] Writing notebook server cookie secret to C:\Users\U
ser\AppData\Roaming\jupyter\runtime\notebook_cookie_secret
[I 11:28:51.340 NotebookApp] JupyterLab extension loaded from C:\Users\User\Anac
onda3\lib\site-packages\jupyterlab
[I 11:28:51.340 NotebookApp] JupyterLab application directory is C:\Users\User\A
naconda3\share\jupyter\lab
[I 11:28:51.559 NotebookApp] Serving notebooks from local directory: C:\
[I 11:28:51.559 NotebookApp] The Jupyter Notebook is running at:
[I 11:28:51.559 NotebookApp] http://localhost:8888/?token=50cf2ad96c88546657f342
14d0519788c5b4adb8ff7fc109
[I 11:28:51.559 NotebookApp] Use Control-C to stop this server and shut down all
 kernels (twice to skip confirmation).
[C 11:28:51.762 NotebookApp]

    Copy/paste this URL into your browser when you connect for the first time,
    to login with a token:
        http://localhost:8888/?token=50cf2ad96c88546657f34214d0519788c5b4adb8ff7
fc109
[I 11:29:14.184 NotebookApp] Accepting one-time-token-authenticated connection f
rom ::1
[I 11:31:08.534 NotebookApp] 302 GET /tree (::1) 8.00ms
[I 11:58:44.766 NotebookApp] Creating new notebook in
[I 11:58:45.201 NotebookApp] Writing notebook-signing key to C:\Users\User\AppDa
ta\Roaming\jupyter\notebook_secret
[W 11:58:45.401 NotebookApp] 403 POST /api/contents (::1): Permission denied: Un
titled.ipynb
[W 11:58:45.403 NotebookApp] Permission denied: Untitled.ipynb
[W 11:58:45.436 NotebookApp] 403 POST /api/contents (::1) 673.24ms referer=http:
//localhost:8888/tree
[I 12:21:01.767 NotebookApp] Interrupted...
[I 12:21:01.767 NotebookApp] Shutting down 0 kernels
