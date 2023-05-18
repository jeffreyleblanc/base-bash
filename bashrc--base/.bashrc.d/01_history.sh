
# don't put duplicate lines or lines starting with space in the history.
# See bash(1) for more options
HISTCONTROL=ignoreboth

# append to the history file, don't overwrite it
shopt -s histappend

# Set history size and format
HISTSIZE=5000
HISTFILESIZE=10000
HISTTIMEFORMAT="%FT%T  "

# For future could experiment with the following:
# export PROMPT_COMMAND="history -a; history -c; history -r; $PROMPT_COMMAND"

# History
function hig() { history | grep "$1"; }
# More history commands (CHECK!)
# Get just unique occurances of a thing
# higu(){ history | grep $1 | cut | sort | uniq ; }
alias h1='history 10'
alias h2='history 20'
alias h3='history 30'
alias h4='history 40'
alias h5='history 50'

# Because history now has extra info, piping to this
# will remove command sequence and date
alias hclean='cut -c 29-'


