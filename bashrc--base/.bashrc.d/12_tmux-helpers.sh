

function tmn(){ tmux new -s $1 "${@:2}"; }
function tmnf(){ tmux new "$@" -s auto-$(uuidgen | cut -c1-4) ; }
function tml(){ tmux ls; }
function tma(){ tmux a -t $1; }
function tmk(){ tmux kill-session -t $1; }
