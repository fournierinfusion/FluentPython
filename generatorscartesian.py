

def makeColors(colors,sizes,text):
    for tshirt in ('%s, %s, %s'% (c,s,r) for c in colors for s in sizes for r in text):
        print(tshirt)








if __name__ == '__main__':
    colors = ['red','gold','blue']
    sizes = ['small','medium','large']
    text = ['start each day','positive vibe']

    makeColors(colors,sizes,text)
    generatorExpression(text)