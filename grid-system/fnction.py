while 1:
      a=[]
      for j in range(0,5):
            z=str(input())
            a.append(z) 
      for k in range(0,5):
            b=(a[k].lower()).replace(' ','-')
            print ("<div class=\"col-51\">\n<a href=\"\"><img src=\"img/thumbs/",b,".jpg\" alt=\"",a[k]," 5by5\">",a[k],"</a>\n</div>",sep='')
