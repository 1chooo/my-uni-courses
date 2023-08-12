function x=substitute(a,n,b)
    x(n)=b(n)/a(n,n);
    for i=n-1:-1:1
        sum=0;
        for j=i+1:n
            sum=sum+a(i,j)*x(j);
        end
        x(i)=(b(i)-sum)/a(i,i);
    end
end

function x=gauss(a,b,n,tol,er)
    er=0;
    for i=1:n
        s(i)=abs(a(i,1));
        for j=2:n
            if abs(a(i,j))>s(i)
                s(i)=abs(a(i,j));
            end
        end
    end
    // Eliminate
    for k=1:n-1
        // pivot
        p=k;
        big=abs(a(k,k)/s(k));
        for ii=k+1:n
            dummy=abs(a(ii,k)/s(ii));
            if dummy>big
                big=dummy;
                p=ii;
            end
        end
        if p~=k
            for jj=k:n
                dummy=a(p,jj);
                a(p,jj)=a(k,jj);
                a(k,jj)=dummy;
            end
            dummy=b(p);
            b(p)=b(k);
            b(k)=dummy;
            dummy=s(p);
            s(p)=s(k);
            s(k)=dummy;
        end
        if abs(a(k,k)/s(k))<tol
            er=-1;
            break
        end
        for i=k+1:n
            factor=a(i,k)/a(k,k);
            for j=k+1:n
                a(i,j)=a(i,j)-factor*a(k,j);
            end
            b(i)=b(i)-factor*b(k);
        end
    end
    if abs(a(n,n)/s(n))<tol
        er=-1;
    end

    if er~=-1
        x=substitute(a,n,b);
    end
end

%test
A=[1,2,-1;5,2,2;-3,5,-1];
B=[2,9,1];
x=gauss(A,B,3,0,0)
x =
   1.00000   1.00000   1.00000