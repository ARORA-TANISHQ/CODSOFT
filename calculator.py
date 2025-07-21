a=float(input("enter 1st operand."))
b=float(input("enter 2nd operand."))
print("Select operator:-\n1:-ADD\n2:-SUBTRACT\n3:-MULTIPLY\n4:-DIVIDE")
c=int(input())
if c==1:{
    print(f"Result => \n{a}+{b}={a+b}")
}
elif c==2:{
    print(f"Result => \n{a}-{b}={a-b}")
}
elif c==3:{
    print(f"Result => \n{a}X{b}={a*b}")
}
elif c==4:
    if b!=0:{
    print(f"Result => \n{a}/{b}={a/b}")
    }
    else:
        {
            print("Division not possible with zero")
        }
else:
    {
        print("Invalid operator")
    }