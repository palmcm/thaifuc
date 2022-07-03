# Thaifuc
Brainfsck but Thai

# Setup
install brainfuck interpreter by

```
pip install brainfuck-interpreter
```

# To use
```
python thaifuc.py <filename> 
python thaifuc.py exmaple.thf
```

# Docs
Just write like Brainfsck but change the command to Thai
|Command|คำสั่ง|
|---|---|
|> | ขวา|
|< |ซ้าย |
|+ |เพิ่ม |
|- |ลด |
|. |พิมพ์ |
|, |ใส่ |
|[ |ข้ามวนถ้าหากว่าช่องที่ชี้อยู่เป็น๐ |
|] |วน |

## Special Feature
When write Brainfsck, we might use many same command in a row.
So we add feature to shorten the code by write number after the command

### Example
```
>>>>+++++ can shorten to ขวา๔เพิ่ม๕
```