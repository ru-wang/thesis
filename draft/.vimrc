set guifont=hack\ 13
set guifontwide=wenquanyi\ micro\ hei\ 13
set fillchars=fold:-
set runtimepath+=./
colo typewriter
let g:gfw_size_diff = 0
let g:airline_theme = 'typewriter'
let g:goyo_width = '100'
call ConfigureTex()
autocmd! User GoyoEnter nested set nolinebreak
