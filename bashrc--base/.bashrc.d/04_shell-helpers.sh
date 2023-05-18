

# Prompt helpers
function zz() { echo -----------------------------------; clear; }
function ps1() { PS1="$1$ "; }
function sclear { clear && printf '\e[3J'; }

# Navigation
alias ..='cd ..'
function .g() {
    # Go to root directory of a git repository
    if git status >/dev/null 2>&1 ; then
        echo "Moving to repository root." ;
        cd $(git rev-parse --show-toplevel) ;
    else
        echo "Outside a git repo" ;
    fi
}
mkcd(){ mkdir -p $1 && cd $1; }

# Review ls shortcuts including
alias la='ls -a'
alias ll='ls -al'
alias l1='ls -1'
# etc...

