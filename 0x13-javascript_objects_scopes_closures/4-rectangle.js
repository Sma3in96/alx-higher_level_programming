#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ( w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      this.width = undefined;
      this.height = undefined;
    }
  }

  print () {
    let w = this.width, h = this.height;
    for (let i = 0; i < h; i++) {
      let str = '';
      for (let j = 0; j < w; j++) {
        str += 'X';
      }
      console.log(str);
    }
  }

  rotate () {
    let temp = this.width;
    this.width = this.height;
    this.height = temp; 
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}

module.exports = Rectangle;
