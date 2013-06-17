customplone.app.locales
=======================

Custom [plone.app.locales](https://github.com/collective/plone.app.locales) Python package
for Plone 4.3. Example: how to override default Plone translations.

Наверняка многим известна особенность [Plone CMS](http://plone.org/products/plone/releases/4.3), заключающаяся в том, что нет никакой возможности
переименовать так называемую «главную» aka «Home» страницу. Некоторые пытаются спрятать вкладку/папку
«Главная», но в breadcrumbs все равно остается ссылка на нее.

Так вот, переименовать папку/страницу «Главная»/«Home» можно. Только делается это слегка перректально,
а именно - через Buildout.

Вкратце, нужно создать свой Python package, добавить в него файлы локализации/интернационализации,
и включить этот пакет в сборку Plone.

Как это сделал я - читайте далее.
Здесь приведен пример добавления пакета в buildout в OS MS Windows. Хочу заметить, в Linux это делается несколько проще.

* Скачал [plone.app.locales](https://github.com/collective/plone.app.locales) и выкинул из него все лишнее.
* Переименовал в customplone.app.locales. Получилась такая раскладка пакета:

<pre>
customplone.app.locales\customplone
customplone.app.locales\MANIFEST.in
customplone.app.locales\setup.py
customplone.app.locales\customplone\app
customplone.app.locales\customplone\__init__.py
customplone.app.locales\customplone\app\locales
customplone.app.locales\customplone\app\__init__.py
customplone.app.locales\customplone\app\locales\configure.zcml
customplone.app.locales\customplone\app\locales\locales
customplone.app.locales\customplone\app\locales\__init__.py
customplone.app.locales\customplone\app\locales\locales\ru
customplone.app.locales\customplone\app\locales\locales\ru\LC_MESSAGES
customplone.app.locales\customplone\app\locales\locales\ru\LC_MESSAGES\plone.po

или, нагляднее

customplone.app.locales
|   MANIFEST.in
|   setup.py
|
\---customplone
    |   __init__.py
    |
    \---app
        |   __init__.py
        |
        \---locales
            |   configure.zcml
            |   __init__.py
            |
            \---locales
                \---ru
                    \---LC_MESSAGES
                            plone.po
</pre>

* Поправил текст в файлах, убрав лишнее и отразив переименование пакета.
* Скопировал пакет (папку customplone.app.locales) в папку src билдаута. Саму папку «src» пришлось создать руками.
* Дописал в buildout.cfg несколько строк:

<pre>
[buildout]
...
eggs =
   Plone
...
   customplone.app.locales

zcml =
    customplone.app.locales

parts =
    instance
...
    precompile

develop =
    src/customplone.app.locales

[instance]
...
environment-vars =
    zope_i18n_compile_mo_files true

[precompile]
recipe = plone.recipe.precompiler
eggs = ${buildout:eggs}
compile-mo-files = true
</pre>

Я мог бы привести здесь diff файл, показывающий разницу между начальным состоянием buildout.cfg и его теперешним состоянием,
но, на мой взгляд, это менее наглядно, ибо в diff не попадают заголовки секций конфига.

* Запустил `bin\buildout` и проверил результат - сайт рабочий и Главная страница уже не Главная.
Переименование прошло успешно.

![ScreenShot](https://raw.github.com/vasnake/customplone.app.locales/master/customplone.screen.png)

Команды (в Windows) для запуска buildout и старта/остановки Plone
<pre>
C:\Plone43\python>python ..\bin\service-zeo.py stop
C:\Plone43\python>python ..\bin\service.py stop
C:\Plone43\python>cd ..
C:\Plone43>bin\buildout
C:\Plone43>cd python
C:\Plone43\python>python ..\bin\service.py start
C:\Plone43\python>python ..\bin\service-zeo.py start
</pre>

Ссылки

* [Internationalization in Plone](http://maurits.vanrees.org/weblog/archive/2010/10/i18n-plone-4#overriding-translations)
* [Original Plone locales package](https://github.com/collective/plone.app.locales)
* [Buildout HOWTO](https://weblion.psu.edu/trac/weblion/wiki/BuildOut)
* [Buildout recipe for 'po' to 'mo' compile](https://github.com/plone/plone.recipe.precompiler)
* [Plone 4 Windows specifics](http://plone.org/documentation/kb/plone-4-windows-installer)
* [Plone 4 debug_mode](http://developer.plone.org/getstarted/debug_mode.html#starting-plone-in-debug-mode-on-microsoft-windows)
