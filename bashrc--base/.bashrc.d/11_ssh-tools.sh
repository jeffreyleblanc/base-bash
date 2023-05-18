

function ssh-status() {
    echo "== SSH ====" ;
    sudo systemctl is-active ssh ;
    echo "== UFW ====" ;
    sudo ufw status | grep --color=never -E 'Status|22' ;
}

function ssh-start() {
    sudo ufw allow 22 ;
    sudo systemctl start ssh ;
}

function ssh-stop() {
    sudo systemctl stop ssh ;
    sudo ufw deny 22 ;
}

function yadd() { ssh-add -s /usr/lib/x86_64-linux-gnu/opensc-pkcs11.so ; }
function yrem() { ssh-add -e /usr/lib/x86_64-linux-gnu/opensc-pkcs11.so ; }

