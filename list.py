

def main():
    List = []
    N = int(input())
    for i in range(0,N):
     cmd = input().split();
     if cmd[0] == "insert":
         List.insert(int(cmd[1]),int(cmd[2]))
     elif cmd[0] == "append":
         List.append(int(cmd[1]))
     elif cmd[0] == "pop":
         List.pop()
     elif cmd[0] == "print":
         print(List)
     elif cmd[0] == "remove":
         List.remove(int(cmd[1]))
     elif cmd[0] == "sort":
         List.sort();
     else:
         List.reverse();

if __name__ == "__main__":
    main()