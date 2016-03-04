Walnut-Compiler
===

### 示例：

+ 假设源代码文件**source.js**的内容如下：

```javascript
// foo is a variable
var foo = 'bar';
function fn() {
    var a = 123;
    a += 456;
    console.log(foo);
}
```

+ 词法分析：

```python
from lex import tokenizer

tokens = tokenizer.parse('./source.js')

for token in tokens:
    print(token, token.val)

print(len(tokens))
```

+ 运行结果：
```
<lex.tokens.Comment object at 0x7f027af4e8d0> [Comment]
<lex.tokens.LT object at 0x7f027af4e6a0> [LT]
<lex.tokens.KeyWord object at 0x7f027af4e6d8> var
<lex.tokens.ID object at 0x7f027af4ef60> foo
<lex.tokens.Assign object at 0x7f027364da20> =
<lex.tokens.String object at 0x7f027af4ef98> bar
<lex.tokens.SemiColon object at 0x7f027364d438> ;
<lex.tokens.LT object at 0x7f027af4eeb8> [LT]
<lex.tokens.KeyWord object at 0x7f027af4ee10> function
<lex.tokens.ID object at 0x7f027af59160> fn
<lex.tokens.OpenParen object at 0x7f027af7a710> (
<lex.tokens.CloseParen object at 0x7f027af7a8d0> )
<lex.tokens.OpenCurly object at 0x7f027af5af60> {
<lex.tokens.LT object at 0x7f027364dd68> [LT]
<lex.tokens.KeyWord object at 0x7f027364de10> var
<lex.tokens.ID object at 0x7f027364ddd8> a
<lex.tokens.Assign object at 0x7f027364da20> =
<lex.tokens.Number object at 0x7f027364dda0> 123
<lex.tokens.SemiColon object at 0x7f027364d438> ;
<lex.tokens.LT object at 0x7f027364de48> [LT]
<lex.tokens.ID object at 0x7f027364deb8> a
<lex.tokens.PlusAssign object at 0x7f027364da58> +=
<lex.tokens.Number object at 0x7f027364df28> 456
<lex.tokens.SemiColon object at 0x7f027364d438> ;
<lex.tokens.LT object at 0x7f027364def0> [LT]
<lex.tokens.ID object at 0x7f027364dfd0> console
<lex.tokens.Dot object at 0x7f027364d400> .
<lex.tokens.ID object at 0x7f0273653080> log
<lex.tokens.OpenParen object at 0x7f027af7a710> (
<lex.tokens.ID object at 0x7f02736530f0> foo
<lex.tokens.CloseParen object at 0x7f027af7a8d0> )
<lex.tokens.SemiColon object at 0x7f027364d438> ;
<lex.tokens.LT object at 0x7f0273653198> [LT]
<lex.tokens.CloseCurly object at 0x7f027af7a898> }
```
