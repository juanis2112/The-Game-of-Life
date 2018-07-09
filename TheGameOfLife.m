

Titulo = ['///////=====================================================///////\n'...
'///////                     WELCOME TO                      ///////\n'...
'///////                                                     ///////\n'...
'///////                  THE GAME OF LIFE                   ///////\n'...
'///////=====================================================///////\n'...
'///////              Presentado por: Juanita Gomez          ///////\n'...
'///////=====================================================///////\n'];
 
separator = '\n///////=====================================================///////';
fprintf(Titulo);
fprintf('\nPresentado Por: Juanita Gomez');
r = input('\nEscoja la probabilidad de que una célula inicie viva: ');
m = input('\nEscoja el tamaño de la matriz cuadrada a usar: ');
state = 0; 
a='#';
b=' ';
%Creación de matriz
TheGameOfLife=char(ones(m));
for i=1:m
    for j=1:m
        y = randi([0 100],1,1);
        if (y>r) 
            TheGameOfLife(i,j)=b;
        else 
            TheGameOfLife(i,j)=a;
        end  
    end
end
%Evolución de la matriz (Ciclo infinito)
while 1>0
    clc;
    fprintf(Titulo);
    fprintf('\nUd escogió una probabilidad inicial de vida del: %d ',r);
    fprintf('\nUd escogió una matriz cuadrada de tamaño: %d', m);
    fprintf(separator);
    display(TheGameOfLife);
    fprintf(separator);
    fprintf('\nState: %d', state);
    fprintf('\nGracias por Jugar\nPara finalizar el juego oprima (ctrl + c)\nHasta la próxima\n');
    state = state + 1; 
    pause(0.1);
    %Cada una de las iteraciones del programa 
    for i=1:m
        for j=1:m
            v=0;
            if i+1<m+1
                if TheGameOfLife(i+1,j)==a 
                    v=v+1;
                end
                if j+1<m+1 
                    if TheGameOfLife(i+1,j+1)==a 
                        v=v+1;
                    end
                end
                if j-1>0 
                    if TheGameOfLife(i+1,j-1)==a 
                        v=v+1; 
                    end
                end
            end
            if i-1>0
                if TheGameOfLife(i-1,j)==a 
                    v=v+1;
                end
                if j+1<m+1
                    if TheGameOfLife(i-1,j+1)==a 
                        v=v+1;
                    end
                end
                if j-1>=1 
                    if TheGameOfLife(i-1,j-1)==a 
                        v=v+1;     
                    end
                end
            end
            if j+1<m+1 
                if TheGameOfLife(i,j+1)==a 
                    v=v+1; 
                end
            end
            if j-1>0
                if TheGameOfLife(i,j-1)==a 
                    v=v+1;
                end
            end
 
            %Encontrar células vivas
            if TheGameOfLife(i,j)==a 
 
                %1Una célula viva con menos de dos vecinos vivos muere
                if v<2 
                    TheGameOfLife(i,j)=b;
                end
                %2Una célula viva con 2 o 3 vecinos vivos permanece en su estado
                if (v==2||v==3) 
                    TheGameOfLife(i,j)=a;
                end
                %3Una celula viva con mas de 3 vecinos muere
                if v>3 
                    TheGameOfLife(i,j)=b;
                end
            end
            %Encontrar células muertos
            if TheGameOfLife(i,j)==b; 
                %4Una celula muerta con exactamente 3 vecinos vivos se convierte en viva
                if v==3 
                    TheGameOfLife(i,j)=a;
                end
            end
        end
    end
end
 