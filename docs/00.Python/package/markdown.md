
## markdown

```bash
pip install markdown
```

```python
In [1]: import markdown                                                                                                                                                 

In [2]: markdown.markdown('|c1|c2|\n|-|-|\n|text1|text2|', extensions=['markdown.extensions.tables'])                                                                   
Out[2]: '<table>\n<thead>\n<tr>\n<th>c1</th>\n<th>c2</th>\n</tr>\n</thead>\n<tbody>\n<tr>\n<td>text1</td>\n<td>text2</td>\n</tr>\n</tbody>\n</table>'
```
