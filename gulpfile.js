var gulp = require('gulp'),
    livereload = require('gulp-livereload');

gulp.task('watch', function() {
    livereload.listen();
    gulp.watch('**/templates/**').on('change', livereload.changed);
});

gulp.task('default', ['watch']);
