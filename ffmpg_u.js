const ffmpegInstaller = require('@ffmpeg-installer/ffmpeg');
const ffmpeg = require('fluent-ffmpeg');

ffmpeg.setFfmpegPath(ffmpegInstaller.path);
var inFilename = "./recorded/dondo.h264";  // 상대주소
var outFilename = "./recorded/dondo.mp4";  // 저장할 위치
ffmpeg(inFilename)
  .outputOptions("-c:v", "copy") // this will copy the data instead or reencode it
  .save(outFilename);
