rm(list=ls())
x1= rnorm(30)
x2 = rnorm(30)
dist(rbind(x1,x2),method="euclidean")
mtcars
cor(mtcars,method="pearson")
USArrests
library(cluster)
library(ggplot2)
data(iris)
iris$Species = as.numeric(iris$Species)
cost_df = data.frame()
for(i in 1:100){
  kmeans = kmeans(x=iris,center=i,iter.max = 50)
  cost_df = rbind(cost_df, cbind(i,kmeans$tot.withinss))
}
names(cost_df) = c("cluster","cost")
ggplot(data=cost_df, aes(x=cluster, y=cost, group=1))+
  theme_bw(base_family = "Garamond")+
  geom_line(colour = "darkgreen")+
  theme(text = element_text(size=20))+
  ggtitle("reduction cost\n")+
  xlab("\nclusters")+
  ylab("with cluster\n")


library(e1071)
sample = iris[sample(nrow(iris)),]
train = sample[1:105,]
test = sample[106:150,]
tune = tune(svm,Species~. , data=train, kernel = "radial",scale=FALSE,
            ranges = list(cost=c(0.001,0.01,0.1,1,5,10,100)))
tune$best.model
summary(tune)
model = svm(Species~.,data=train,kernel="radial",cost=10,scale=FALSE)
predict(model,test)




install.packages("recommenderlab")
library(recommenderlab)
set.seed(1)

data_package = data(package="recommenderlab")
data_package$results[,"Item"]
data(MovieLense)
methods(class=class(MovieLense))
similarity_users = similarity(MovieLense[1:4,],method="cosine",which="users")
as.matrix(similarity_users)
x11()
image(as.matrix(similarity_items))
similarity_items = similarity(MovieLense[,1:4],method = "cosine", which = "items")
as.matrix(similarity_items)


recommender_models = recommenderRegistry$get_entries(dataType = "realRatingMatrix")
names(recommender_models)
dim(MovieLense)
vector_rating = as.vector(MovieLense@data)
unique(vector_rating)
table_rating = table(vector_rating)
vector_rating = as.factor(vector_rating)
views_per_movie = colCounts(MovieLense)
table_views = data.frame(movie = names(views_per_movie),views = views_per_movie)
table_views  = table_views[order(table_views$views,decreasing = TRUE),]

average_rating = colMeans(MovieLense)
average_rating_relevant = average_rating[views_per_movie>100]
