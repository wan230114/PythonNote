
# tmux配置

tmux配置：

[gpakosz/.tmux: 🇫🇷 Oh my tmux! My self-contained, pretty & versatile tmux configuration made with ❤️](https://github.com/gpakosz/.tmux)

```bash
git clone https://github.com/gpakosz/.tmux.git $PWD
ln -s -f $PWD/.tmux.conf ~/.tmux.conf
cp $PWD/.tmux.conf.local ~/.tmux.conf.local

{
echo "
# switch windows alt+number
bind-key -n M-1 select-window -t 1
bind-key -n M-2 select-window -t 2
bind-key -n M-3 select-window -t 3
bind-key -n M-4 select-window -t 4
bind-key -n M-5 select-window -t 5
bind-key -n M-6 select-window -t 6
bind-key -n M-7 select-window -t 7
bind-key -n M-8 select-window -t 8
bind-key -n M-9 select-window -t 9
# switch between tabs with alt+larrow && alt+rarrow
bind-key -n M-a last-window
bind-key -n M-z prev
bind-key -n M-x next
# switch between tabs with alt+larrow && alt+rarrow
#bind-key -n C-S-Left prev
#bind-key -n C-S-Right next

# 默认tmux貌似不允许鼠标滚动，不滚动就不好查之前的命令输出信息。
set-window-option -g mode-mouse on
# # Make mouse useful in copy mode
# setw -g mode-mouse on

# Allow mouse to select which pane to use
set -g mouse-select-pane on
" >>~/.tmux.conf.local
}
```

## 简易教程

[1. TMUX commands — TMUX Guide documentation](https://tmuxguide.readthedocs.io/en/latest/tmux/tmux.html)

```bash
tmux new -s install
```

# screen

