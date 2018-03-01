'use strict';

var gulp = require('gulp');
var sass = require('gulp-sass');


gulp.task('sass', function () {
  gulp.src('./djangokibana/static/scss/**/*.scss')
    .pipe(sass({
      outputStyle: 'expanded',
      // includePaths: require('node-normalize-scss').includePaths
    }))
    .pipe(gulp.dest('./djangokibana/static/css/'));
});

gulp.task('sass:watch', function () {
  gulp.watch('./djangokibana/static/scss/**/*.scss', ['sass']);
});

gulp.task('watch',function() {
    gulp.watch('djangokibana/static/scss//**/*.scss',['sass']);
});

gulp.task('default', ['sass', 'watch'])
