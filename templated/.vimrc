set guifont=hack\ 13
set guifontwide=wenquanyi\ micro\ hei\ 13
set fillchars=fold:-
set runtimepath+=../
colo ayu
let g:gfw_size_diff = 0
let g:airline_theme = 'ayu'
let g:goyo_width = '100'
call ConfigureTex()
autocmd! User GoyoEnter nested set nolinebreak
autocmd! User GoyoLeave nested set nolinebreak
