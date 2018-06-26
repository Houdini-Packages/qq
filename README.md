*This repository is described here: http://lex.ikoon.cz*

*I hope that some of the Python or VEX functions will help you. Some of them are mine, some of them are collected and I [THANK YOU](http://lex.ikoon.cz/thanks/) very much, all the authors and great community. I could not do this without you. I will record a video description asap.*


# files and folders 

#### toolbar
- this folder contains:
    - one shelf set (`wf__set.shelf`)
    - twelve shelves (`wf_chaneditor.shelf`, `wf_render.shelf`, etc.)
- each shelve contains tools, and each tool calls a specific function
- some of the tools have their hotkey, other are accessible by the TAB menu
 
#### python2.7libs
- this folder contains python functions
- here is described what each function does: 
  - http://lex.ikoon.cz/network_parm
  - http://lex.ikoon.cz/network_ui
  - etc.

#### vex
- this folder contains:
  - `uber.vfl` - a source for "uber parse" as described here: http://lex.ikoon.cz/vex-uber-parse
  - `qq.vfl` - library of custom functions, to be #included in a wrangle
  - `triggers.db` - library of triggers, more described here: http://lex.ikoon.cz/vex-ui-markup
  - `snippets.db` - library of snippets
  - `helpcard.txt` - just a helpcard

#### Houdini.keymap.overrides
- this file is set of my custom hotkeys

#### PARMmenu.xml
- this file customizes the Parameter context menu (right click on any Parameter)

# instalation
- copy the files into `$HOUDINI_USER_PREF_DIR`
- on Windows it is typically `C:\Users\your_user_name\Documents\houdini16.5`