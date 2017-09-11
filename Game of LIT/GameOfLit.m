function GameOfLit(length, height, bound, unbound, genNum,time_pause)
% initialise the model framework
% height =  number of cells along the y axis
% length = number of cells along x axis
% gen = the number of generations
% bound = percentage of bound cells
% timePause = time gap between each graph
% define the size of the matrix (grid)
M = zeros(length,height);
for i=1:length;
    for j=1:height;
        if rand<= bound;%generate a random number of cells betweeen 0 
            M(i,j)=1;
     
        end
    end
end 
% define the number of each cell state
% assume 100% of the grid is filled, i.e. no empty cells
totalCells= length*height;
boundNum= bound*totalCells;
unboundNum= unbound*totalCells;
emptyNum= 1-(boundNum+ unboundNum); 
%error catching
if bound >1 || unbound > 1
    disp('enter a percentage value between 0 and 1')
    return
end
%display the grid of cells
%figure('Game of LIT')
colormap(gray(2));
image(2*(1-M) );
pause(time_pause);
%defining placeholders for plotting time course data
time = [];
cellCount = [];
counter = 0;
%find the neirest neighbours, in horizontal and vertical direction
for g=1:genNum;
    for i=1:length; %for all cells in x axis
        for j=1:height; %for all cells in y axis
            grid =1; %cells which are still white (available to bind)
            for a=i-1:i+1; %find horizontal neighbours of i
                for b=j-1:j+1; %find vertical neighbours of j
                    if a >= 1 && b >= 1 && a <= length && b <= height
                        if a==i && b==j; %don't consider these elements
                        else
                            grid= grid + M(a,b);
                        end
                    end
                end
                neighbour (i,j)= grid; %function of neighbours of cells (i,j)
            end
        end
    end
    
    load('S_2.mat')
   
    % update the grid 
    % define the rules of the game 
    for i=1:length;
        for j=1:height;
            if neighbour(i,j)==1 %for 1 neighbour 
                if rand<= 0.30*S_2(g,2) %generate random numbers btw 1 and 2, 50% will bind
                    M(i,j)=1;
                else M(i,j)=M(i,j);
                end
            elseif neighbour(i,j)==2; 
                if rand<=0.60*S_2(g,2);
                    M(i,j)=1; 
                else M(i,j)=M(i,j);
                end 
            elseif  neighbour(i,j)==3; 
                if rand<= 0.80*S_2(g,2); 
                    M(i,j)=1;
                else M(i,j)=M(i,j);
                end 
            elseif neighbour(i,j)==4;
                if rand<=0.99*S_2(g,2);
                    M(i,j)=1;
                else M(i,j)=M(i,j);
                end
            else neighbour(i,j)=0;
                if rand<=0.2*S_2(g,2);
                    M(i,j)=1;
                else M(i,j)=M(i,j);
                end
            end
        end
    end
    image(2*(1-M));
    pause(time_pause);
    
    %incrementing the counters and pushing the data
    cellCount(end+1)=sum(sum(M));
    time(end+1)= counter;
    
    counter = counter + 1;
    disp(sum(sum(M))) 
   
end
%plot(time,cellCount)
for bound= 0.2
    for unbound=0.05
        figure(2)
        plot (time, cellCount)
        xlabel ('Time points')
        ylabel ('Number of cells bound')
        hold on
    end 
end
end