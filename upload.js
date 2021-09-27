let runPy = new Promise(function(success, nosuccess) {

  const { spawn } = require('child_process');       //자식프로세스를 지정하여 실행
  const pyprog = spawn('node', ['./ffmpg_u.js']);   //자식프로세스로 지정

  pyprog.stdout.on('data', function(data) {

      success(data);
  });

  pyprog.stderr.on('data', (data) => {

      nosuccess(data);
  });
});
const fs=require('fs');
const AWS = require('aws-sdk');     //aws와 연동하는데 필요한 모듈을 가져옴
const id = '';                //id key값 
const pw = '';                //key값 password
const bucket_name = '';      //bucket 이름
const s3=new AWS.S3({
  accessKeyId: id,
  secretAccessKey: pw
});
const uploadFile = (fileName) => {                 //s3에 업로드하는 함수
  const fileContent = fs.readFileSync(fileName);
  const params = {
    Bucket: bucket_name,
    Key: 'dondo.mp4',
    Body: fileContent,
    ACL: 'public-read',
    ContentType: "video/mp4"
  };
  s3.upload(params, function(err,data){
    if(err) {throw err;}
    console.log(`file uploaded successfully. ${data.Location}`);
  });
};
uploadFile('./recorded/dondo.mp4');         /함수호출 경로
