安装sphinx的过程
===============

.. code-block:: bash
   (f:\MyGame\TraeFuck\TraeSecond\PyGameSun\.conda) F:\MyGame\TraeFuck\TraeSecond\PyGameSun>sphinx-quickstart docs
   Welcome to the Sphinx 8.2.3 quickstart utility.

   Please enter values for the following settings (just press Enter to
   accept a default value, if one is given in brackets).

   Selected root path: docs

   You have two options for placing the build directory for Sphinx output.
   Either, you use a directory "_build" within the root path, or you separate
   "source" and "build" directories within the root path.
   > Separate source and build directories (y/n) [n]: y

   The project name will occur in several places in the built documentation.
   > Project name: 我和所有本科美女同学发生了性关系
   > Author name(s): 玉蝶游龙
   > Project release []: 1.0

   If the documents are to be written in a language other than English,
   you can select a language here by its language code. Sphinx will then
   translate text that it generates into that language.

   For a list of supported codes, see
   https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language.
   > Project language [en]: zh_CN

   Creating file F:\MyGame\TraeFuck\TraeSecond\PyGameSun\docs\source\conf.py.
   Creating file F:\MyGame\TraeFuck\TraeSecond\PyGameSun\docs\source\index.rst.
   Creating file F:\MyGame\TraeFuck\TraeSecond\PyGameSun\docs\Makefile.
   Creating file F:\MyGame\TraeFuck\TraeSecond\PyGameSun\docs\make.bat.

   Finished: An initial directory structure has been created.

   You should now populate your master file F:\MyGame\TraeFuck\TraeSecond\PyGameSun\docs\source\index.rst and create other documentation
   source files. Use the Makefile to build the docs, like so:
      make builder
   where "builder" is one of the supported builders, e.g. html, latex or linkcheck.

构建Html的警告
=============

.. code-block:: bash

   (f:\MyGame\TraeFuck\TraeSecond\PyGameSun\.conda) F:\MyGame\TraeFuck\TraeSecond\PyGameSun\docs>make html
   Running Sphinx v8.2.3
   loading translations [zh_CN]... done
   making output directory... done
   building [mo]: targets for 0 po files that are out of date
   writing output...
   building [html]: targets for 3 source files that are out of date
   updating environment: [new config] 3 added, 0 changed, 0 removed
   reading sources... [100%] usage
   F:\MyGame\TraeFuck\TraeSecond\PyGameSun\docs\source\installprocess.rst:2: WARNING: Title underline too short.

   安装sphinx的过程
   =============== [docutils]
   F:\MyGame\TraeFuck\TraeSecond\PyGameSun\docs\source\installprocess.rst:4: ERROR: Error in "code-block" directive:
   maximum 1 argument(s) allowed, 11 supplied.

.. code-block:: bash
   (f:\MyGame\TraeFuck\TraeSecond\PyGameSun\.conda) F:\MyGame\TraeFuck\TraeSecond\PyGameSun>sphinx-quickstart docs
   Welcome to the Sphinx 8.2.3 quickstart utility.

   Please enter values for the following settings (just press Enter to
   accept a default value, if one is given in brackets).

   Selected root path: docs

   You have two options for placing the build directory for Sphinx output.
   Either, you use a directory "_build" within the root path, or you separate
   "source" and "build" directories within the root path.
   > Separate source and build directories (y/n) [n]: y

   The project name will occur in several places in the built documentation.
   > Project name: 我和所有本科美女同学发生了性关系
   > Author name(s): 玉蝶游龙
   > Project release []: 1.0

   If the documents are to be written in a language other than English,
   you can select a language here by its language code. Sphinx will then
   translate text that it generates into that language.

   For a list of supported codes, see
   https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-language.
   > Project language [en]: zh_CN

   Creating file F:\MyGame\TraeFuck\TraeSecond\PyGameSun\docs\source\conf.py.
   Creating file F:\MyGame\TraeFuck\TraeSecond\PyGameSun\docs\source\index.rst.
   Creating file F:\MyGame\TraeFuck\TraeSecond\PyGameSun\docs\Makefile.
   Creating file F:\MyGame\TraeFuck\TraeSecond\PyGameSun\docs\make.bat.

   Finished: An initial directory structure has been created.

   You should now populate your master file F:\MyGame\TraeFuck\TraeSecond\PyGameSun\docs\source\index.rst and create other documentation
   source files. Use the Makefile to build the docs, like so:
      make builder
   where "builder" is one of the supported builders, e.g. html, latex or linkcheck. [docutils]
   looking for now-outdated files... none found
   pickling environment... done
   checking consistency... done
   preparing documents... done
   copying assets...
   copying static files...
   Writing evaluated template result to F:\MyGame\TraeFuck\TraeSecond\PyGameSun\docs\build\html\_static\basic.css
   Writing evaluated template result to F:\MyGame\TraeFuck\TraeSecond\PyGameSun\docs\build\html\_static\documentation_options.js
   Writing evaluated template result to F:\MyGame\TraeFuck\TraeSecond\PyGameSun\docs\build\html\_static\language_data.js
   copying static files: done
   copying extra files...
   copying extra files: done
   copying assets: done
   writing output... [100%] usage
   generating indices... genindex done
   writing additional pages... search done
   dumping search index in Chinese (code: zh)... done
   dumping object inventory... done

   ====================== slowest reading durations =======================
   0.047 index
   0.031 installprocess
   0.000 usage
   build succeeded, 2 warnings.

   The HTML pages are in build\html.

安装指南
========

本文档提供了安装PyGameSun项目所需的详细步骤。

系统要求
--------

在开始安装之前，请确保您的系统满足以下要求：

- Python 3.12
- pip (Python包管理器)
- Git

安装步骤
--------

克隆代码仓库
~~~~~~~~~~~~

首先，使用Git克隆项目代码：

.. code-block:: bash

    git clone https://github.com/tonggexin/My-AI-Practice.git
    cd My-AI-Practice

创建虚拟环境
~~~~~~~~~~~~

推荐使用conda创建独立的Python虚拟环境：

.. code-block:: bash

    # 使用conda创建虚拟环境
    conda create -n pygame_env python=3.12
    conda activate pygame_env
    
    # 或者使用venv
    python -m venv pygame_env
    # Windows激活方式
    pygame_env\Scripts\activate
    # Linux/MacOS激活方式
    # source pygame_env/bin/activate

安装依赖
~~~~~~~~

使用pip安装项目所需的依赖包：

.. code-block:: bash

    pip install -r requirement.txt

验证安装
~~~~~~~~

运行以下命令验证pygame是否正确安装：

.. code-block:: bash

    python check_pygame.py

如果安装成功，您将看到pygame相关信息的输出。

常见问题
--------

1. **找不到SDL2库**
   
   如果出现SDL2相关错误，请确保已安装SDL2库。在Windows上，pygame包通常会包含所需的DLL文件。

2. **Python版本不兼容**
   
   请确保使用Python 3.12版本，这是项目推荐的版本。

3. **权限问题**
   
   在安装过程中遇到权限错误时，可以尝试使用管理员权限（Windows）或sudo（Linux/MacOS）运行命令。

获取支持
--------

如果您在安装过程中遇到任何问题，可以通过以下方式获取帮助：

- 查阅项目的README文件
- 在GitHub上提交Issue
- 参考pygame官方文档

下一步
------

成功安装后，您可以查看 :doc:`usage` 文档了解如何使用本项目。