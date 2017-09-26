var app = angular.module('app', ['ngAnimate']);
app.controller('c', function($scope) {
	$scope.navClick = true;
    $scope.work = works;
    /*Dependiendo de que se seleccione aparecera la seccion.*/
    $scope.show = function($event){
    	/*Ocultando el mensaje de inicio.*/
    	$scope.navClick = false;
    	/*Consiguiendo la seccion a mostrar por medio del id*/
		$scope.selection = event.target.id;
    }
    /*Datos de modal*/
    $scope.showM = function(n) {
    	 /*Array en /js/works.js*/
         $scope.titulo_modal = works[n].titulo;
         $scope.desc_modal = works[n].description;
         $scope.vid = works[n].video;
         console.log($scope.vid);
    };
});