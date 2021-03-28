logging模块的使用

```python
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s %(levelname)s - %(message)s')
# 其他参数，filename='new.log', filemode='a',  # 写模式"w"或"a"，默认为a
logging.debug('Start of program')
logging.debug('do somethings.')
logging.debug('End of program')
```

