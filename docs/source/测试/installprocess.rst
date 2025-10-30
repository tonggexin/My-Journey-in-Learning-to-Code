安装sphinx的过程
=================

成功安装
--------
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
---------------

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
