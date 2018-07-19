Plover Japanese Sokutaipu
=====================

The Sokutaipu Japanese Realtime stenography system for Plover.

Activating Sokutaipu
~~~~~~~~~~~~~~~~~~~~

After installing this plugin, you need to turn on Sokutaipu in Plover:

1. In Plover's configuration, go to the ``Systems`` tab, and change the active system to ``Japanese Sokutaipu``.
2. You will need a Tréal machine to use this theory.

Common Commands
~~~~~~~~~~~~~~~

It would be a good time to define some custom commands that make using Plover much easier! Just open the add translation dialog, then enter in the steno you want to use to make the command, and enter the following as translation:

- ``{PLOVER:ADD_TRANSLATION}`` this will let you use a chord to summon the add translation dialog
- ``{-|}`` capitalize next word
- ``{^^}`` suppress space
- ``{#right}``, ``{#left}``, ``{#up}``, ``{#down}`` press arrow keys: right, left, up, down (recommendation is to create an arrow-key cluster on one hand with a chord on the other)
- ``{#control(c)}`` copy on Windows, Linux, or ``{#command(c)}`` for Mac
- ``{#control(v)}`` paste on Windows, Linux, or ``{#command(v)}`` for Mac
- ``{#control(z)}`` undo on Windows, Linux, or ``{#command(z)}`` for Mac
- ``{#tab}`` press the tab key
- ``{#alt(tab tab)}`` change application on Windows
- ``{#backspace}`` press the backspace key
- ``{#escape}`` press the escape key
- ``{#return}`` press the return/enter key
- ``{^\n^}{-|}`` new line, capitalize
- ``{^\n\n^}{-|}`` new paragraph, capitalize
