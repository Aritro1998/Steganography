import Encode
import Decode

while True:
    print("1->Encode\n2->Decode\n3->Exit")
    ch = input(" Enter your choice: ")
    if ch == '1':
        Encode.encode.encode()
    elif ch == '2':
        Decode.decode.decode()
    elif ch == '3':
        break
    else:
        print("Wrong Input.... Enter again")
