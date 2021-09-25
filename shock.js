let runPy = new Promise(function(success, nosuccess) {

  const { spawn } = require('child_process');
  const pyprog = spawn('node', ['./ffmpg_s.js']);

  pyprog.stdout.on('data', function(data) {

      success(data);
  });

  pyprog.stderr.on('data', (data) => {

      nosuccess(data);
  });
});
const fs=require('fs');
const AWS = require('aws-sdk');
const id = 'AKIAXU3SCGJX3KBU42EI';
const pw = 'M36CFGm1CeW2LHIaNbdh0zyn7JXcqRsFOrLK7mr/';
const bucket_name = 'lifeflavor';
const s3=new AWS.S3({
  accessKeyId: id,
  secretAccessKey: pw
});
const uploadFile = (fileName) => {
  const fileContent = fs.readFileSync(fileName);
  const params = {
    Bucket: bucket_name,
    Key: 'dondo_s.mp4',
    Body: fileContent,
    ACL: 'public-read',
    ContentType: "video/mp4"
  };
  s3.upload(params, function(err,data){
    if(err) {throw err;}
    console.log(`file uploaded successfully. ${data.Location}`);
  });
};
uploadFile('./recorded/dondo_s.mp4');
