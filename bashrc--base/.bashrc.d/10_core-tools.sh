

# More new
alias ipnow='ip --brief -4 address'
alias fd='fdfind'
alias trash='gio trash'
alias grsync='rsync -avz --delete --exclude=".git/"'

# clipboard
# can xcp use a wl???
function xcp(){ xclip -sel clip; }
function here(){ pwd | xcp; }
function there(){ cd $(wl-paste) ; }


# Finders
fnd() { find . -name $1 ; }

# Openssl wrappers
function sec_lock() { openssl aes-256-cbc -a -salt -in $1 -out $1.enc && rm $1 ; }
function sec_view() { openssl aes-256-cbc -a -d -in $1 ; }
function sec_unlock() { openssl aes-256-cbc -a -d -in $1 -out $2 ; }

# Other
utcnow(){ python3 -c 'import datetime; print(datetime.datetime.utcnow().isoformat())'; }
#> There is a non python way to do this

function ttree(){ tree | sed 's/├\|─\|│\|└/ /g' ; }

