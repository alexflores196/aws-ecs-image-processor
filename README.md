{\rtf1\ansi\ansicpg1252\cocoartf2822
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica-Bold;\f1\fswiss\fcharset0 Helvetica;\f2\fswiss\fcharset0 Helvetica-Oblique;
\f3\fnil\fcharset0 LucidaGrande;\f4\fnil\fcharset128 HiraginoSans-W3;}
{\colortbl;\red255\green255\blue255;\red21\green21\blue22;\red13\green62\blue197;\red69\green73\blue76;
\red228\green234\blue244;\red246\green249\blue252;\red236\green241\blue247;\red109\green109\blue109;}
{\*\expandedcolortbl;;\cssrgb\c10588\c10980\c11373;\cssrgb\c4314\c34118\c81569;\cssrgb\c34118\c35686\c37255;
\cssrgb\c91373\c93333\c96471;\cssrgb\c97255\c98039\c99216;\cssrgb\c94118\c95686\c97647;\cssrgb\c50196\c50196\c50196;}
{\*\listtable{\list\listtemplateid1\listhybrid{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{disc\}}{\leveltext\leveltemplateid1\'01\uc0\u8226 ;}{\levelnumbers;}\fi-360\li720\lin720 }{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{circle\}}{\leveltext\leveltemplateid2\'01\uc0\u9702 ;}{\levelnumbers;}\fi-360\li1440\lin1440 }{\listname ;}\listid1}
{\list\listtemplateid2\listhybrid{\listlevel\levelnfc0\levelnfcn0\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{decimal\}}{\leveltext\leveltemplateid101\'01\'00;}{\levelnumbers\'01;}\fi-360\li720\lin720 }{\listname ;}\listid2}
{\list\listtemplateid3\listhybrid{\listlevel\levelnfc0\levelnfcn0\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{decimal\}}{\leveltext\leveltemplateid201\'01\'00;}{\levelnumbers\'01;}\fi-360\li720\lin720 }{\listname ;}\listid3}}
{\*\listoverridetable{\listoverride\listid1\listoverridecount0\ls1}{\listoverride\listid2\listoverridecount0\ls2}{\listoverride\listid3\listoverridecount0\ls3}}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sa160\partightenfactor0

\f0\b\fs44 \cf2 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 AWS Cloud Image Processor: A Serverless, Auto-Scaling Web Application\
\pard\pardeftab720\sa320\partightenfactor0

\f1\b0\fs32 \cf2 A comprehensive, cloud-native web application built on AWS that allows users to upload images, view detailed metadata, perform conversions, and download the results.\
\pard\pardeftab720\sa160\partightenfactor0

\f0\b\fs40 \cf2 Architecture Diagram\
\pard\pardeftab720\sa320\partightenfactor0

\f2\i\b0\fs32 \cf2 To create your own diagram, I highly recommend using a free tool like {\field{\*\fldinst{HYPERLINK "https://app.diagrams.net/"}}{\fldrslt \cf3 \ul \ulc3 \strokec3 diagrams.net}} (formerly draw.io). You can create a diagram that looks like the one below and export it as a 
\fs28 \cf4 \cb5 \strokec4 .png
\fs32 \cf2 \cb1 \strokec2  to include here.
\f1\i0 \

\f2\i (Replace the link above with a link to your own architecture diagram image)
\f1\i0 \
\pard\pardeftab720\sa160\partightenfactor0

\f0\b\fs40 \cf2 Key Features\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sa160\partightenfactor0
\ls1\ilvl0
\f1\b0\fs32 \cf2 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Session-Based User Experience: Each user gets a private, temporary workspace. Images are isolated per session and automatically cleaned up after 24 hours using S3 Lifecycle Policies.\
\ls1\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Advanced Image Processing:\
\pard\tx940\tx1440\pardeftab720\li1440\fi-1440\sa160\partightenfactor0
\ls1\ilvl1\cf2 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	
\f3 \uc0\u9702 
\f1 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Automatic Thumbnail Generation: An event-driven AWS Lambda function instantly creates thumbnails upon image upload.\
\ls1\ilvl1\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	
\f3 \uc0\u9702 
\f1 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Detailed Metadata Extraction: The Lambda function extracts and stores both basic (size, format) and enhanced EXIF (camera model, settings) metadata in DynamoDB.\
\ls1\ilvl1\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	
\f3 \uc0\u9702 
\f1 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 On-the-Fly Conversion: Users can convert images to various popular formats (JPG, PNG, WEBP, etc.) and resize them to custom dimensions before downloading.\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sa160\partightenfactor0
\ls1\ilvl0\cf2 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 High Availability & Auto-Scaling: The application is deployed on ECS Fargate, a serverless container engine, across multiple Availability Zones. It automatically scales the number of running tasks based on CPU utilization to handle traffic spikes efficiently.\
\ls1\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Robust Security:\
\pard\tx940\tx1440\pardeftab720\li1440\fi-1440\sa160\partightenfactor0
\ls1\ilvl1\cf2 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	
\f3 \uc0\u9702 
\f1 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Network Isolation: All resources are deployed within a custom, secure Amazon VPC with public and private subnets.\
\ls1\ilvl1\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	
\f3 \uc0\u9702 
\f1 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Web Application Firewall (WAF): An AWS WAF is attached to the Application Load Balancer to protect against common web threats like SQL injection and cross-site scripting.\
\ls1\ilvl1\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	
\f3 \uc0\u9702 
\f1 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Principle of Least Privilege: IAM roles are finely tuned to grant each service only the permissions it needs to function.\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sa160\partightenfactor0
\ls1\ilvl0\cf2 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Fully Automated CI/CD Pipeline:\
\pard\tx940\tx1440\pardeftab720\li1440\fi-1440\sa160\partightenfactor0
\ls1\ilvl1\cf2 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	
\f3 \uc0\u9702 
\f1 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 A multi-stage AWS CodePipeline automates the entire deployment process.\
\ls1\ilvl1\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	
\f3 \uc0\u9702 
\f1 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Pushing code to the 
\fs28 \cf4 \cb5 \strokec4 main
\fs32 \cf2 \cb1 \strokec2  branch on GitHub automatically triggers AWS CodeBuild.\
\ls1\ilvl1\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	
\f3 \uc0\u9702 
\f1 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 CodeBuild builds the Docker image for the web app and the deployment package for the Lambda function in parallel.\
\ls1\ilvl1\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	
\f3 \uc0\u9702 
\f1 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 The pipeline then automatically deploys the new versions to Amazon ECS and AWS Lambda with zero downtime.\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sa160\partightenfactor0
\ls1\ilvl0\cf2 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Infrastructure as Code (IaC): The core network, security, and database infrastructure is defined declaratively using AWS CloudFormation, enabling consistent and repeatable environment creation.\
\pard\pardeftab720\sa160\partightenfactor0

\f0\b\fs40 \cf2 Technology Stack\

\itap1\trowd \taflags0 \trgaph108\trleft-108 \trcbpat7 \tamarb640 \trbrdrt\brdrnil \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalc \clcbpat6 \clwWidth3112\clftsWidth3 \clmart10 \clmarl10 \clmarb10 \clmarr10 \clbrdrt\brdrs\brdrw20\brdrcf2 \clbrdrl\brdrs\brdrw20\brdrcf2 \clbrdrb\brdrs\brdrw20\brdrcf2 \clbrdrr\brdrs\brdrw20\brdrcf2 \clpadt160 \clpadl240 \clpadb160 \clpadr240 \gaph\cellx4320
\clvertalc \clcbpat6 \clwWidth11080\clftsWidth3 \clmart10 \clmarl10 \clmarb10 \clmarr10 \clbrdrt\brdrs\brdrw20\brdrcf2 \clbrdrl\brdrs\brdrw20\brdrcf2 \clbrdrb\brdrs\brdrw20\brdrcf2 \clbrdrr\brdrs\brdrw20\brdrcf2 \clpadt160 \clpadl240 \clpadb160 \clpadr240 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0

\f1\b0\fs28 \cf2 Category\cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf2 Technology / Service\cell \row

\itap1\trowd \taflags0 \trgaph108\trleft-108 \trcbpat7 \tamarb640 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalc \clcbpat6 \clwWidth3112\clftsWidth3 \clmart10 \clmarl10 \clmarb10 \clmarr10 \clbrdrt\brdrs\brdrw20\brdrcf2 \clbrdrl\brdrs\brdrw20\brdrcf2 \clbrdrb\brdrs\brdrw20\brdrcf2 \clbrdrr\brdrs\brdrw20\brdrcf2 \clpadt160 \clpadl240 \clpadb160 \clpadr240 \gaph\cellx4320
\clvertalc \clcbpat6 \clwWidth11080\clftsWidth3 \clmart10 \clmarl10 \clmarb10 \clmarr10 \clbrdrt\brdrs\brdrw20\brdrcf2 \clbrdrl\brdrs\brdrw20\brdrcf2 \clbrdrb\brdrs\brdrw20\brdrcf2 \clbrdrr\brdrs\brdrw20\brdrcf2 \clpadt160 \clpadl240 \clpadb160 \clpadr240 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf2 Compute\cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf2 AWS Fargate (for ECS), AWS Lambda\cell \row

\itap1\trowd \taflags0 \trgaph108\trleft-108 \trcbpat7 \tamarb640 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalc \clcbpat6 \clwWidth3112\clftsWidth3 \clmart10 \clmarl10 \clmarb10 \clmarr10 \clbrdrt\brdrs\brdrw20\brdrcf2 \clbrdrl\brdrs\brdrw20\brdrcf2 \clbrdrb\brdrs\brdrw20\brdrcf2 \clbrdrr\brdrs\brdrw20\brdrcf2 \clpadt160 \clpadl240 \clpadb160 \clpadr240 \gaph\cellx4320
\clvertalc \clcbpat6 \clwWidth11080\clftsWidth3 \clmart10 \clmarl10 \clmarb10 \clmarr10 \clbrdrt\brdrs\brdrw20\brdrcf2 \clbrdrl\brdrs\brdrw20\brdrcf2 \clbrdrb\brdrs\brdrw20\brdrcf2 \clbrdrr\brdrs\brdrw20\brdrcf2 \clpadt160 \clpadl240 \clpadb160 \clpadr240 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf2 Storage\cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf2 Amazon S3, Amazon DynamoDB\cell \row

\itap1\trowd \taflags0 \trgaph108\trleft-108 \trcbpat7 \tamarb640 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalc \clcbpat6 \clwWidth3112\clftsWidth3 \clmart10 \clmarl10 \clmarb10 \clmarr10 \clbrdrt\brdrs\brdrw20\brdrcf2 \clbrdrl\brdrs\brdrw20\brdrcf2 \clbrdrb\brdrs\brdrw20\brdrcf2 \clbrdrr\brdrs\brdrw20\brdrcf2 \clpadt160 \clpadl240 \clpadb160 \clpadr240 \gaph\cellx4320
\clvertalc \clcbpat6 \clwWidth11080\clftsWidth3 \clmart10 \clmarl10 \clmarb10 \clmarr10 \clbrdrt\brdrs\brdrw20\brdrcf2 \clbrdrl\brdrs\brdrw20\brdrcf2 \clbrdrb\brdrs\brdrw20\brdrcf2 \clbrdrr\brdrs\brdrw20\brdrcf2 \clpadt160 \clpadl240 \clpadb160 \clpadr240 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf2 Networking & Security\cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf2 Amazon VPC, Application Load Balancer, AWS WAF, IAM\cell \row

\itap1\trowd \taflags0 \trgaph108\trleft-108 \trcbpat7 \tamarb640 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalc \clcbpat6 \clwWidth3112\clftsWidth3 \clmart10 \clmarl10 \clmarb10 \clmarr10 \clbrdrt\brdrs\brdrw20\brdrcf2 \clbrdrl\brdrs\brdrw20\brdrcf2 \clbrdrb\brdrs\brdrw20\brdrcf2 \clbrdrr\brdrs\brdrw20\brdrcf2 \clpadt160 \clpadl240 \clpadb160 \clpadr240 \gaph\cellx4320
\clvertalc \clcbpat6 \clwWidth11080\clftsWidth3 \clmart10 \clmarl10 \clmarb10 \clmarr10 \clbrdrt\brdrs\brdrw20\brdrcf2 \clbrdrl\brdrs\brdrw20\brdrcf2 \clbrdrb\brdrs\brdrw20\brdrcf2 \clbrdrr\brdrs\brdrw20\brdrcf2 \clpadt160 \clpadl240 \clpadb160 \clpadr240 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf2 CI/CD Pipeline\cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf2 AWS CodePipeline, AWS CodeBuild, AWS CodeStar Connections, Amazon ECR, GitHub\cell \row

\itap1\trowd \taflags0 \trgaph108\trleft-108 \trcbpat7 \tamarb640 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalc \clcbpat6 \clwWidth3112\clftsWidth3 \clmart10 \clmarl10 \clmarb10 \clmarr10 \clbrdrt\brdrs\brdrw20\brdrcf2 \clbrdrl\brdrs\brdrw20\brdrcf2 \clbrdrb\brdrs\brdrw20\brdrcf2 \clbrdrr\brdrs\brdrw20\brdrcf2 \clpadt160 \clpadl240 \clpadb160 \clpadr240 \gaph\cellx4320
\clvertalc \clcbpat6 \clwWidth11080\clftsWidth3 \clmart10 \clmarl10 \clmarb10 \clmarr10 \clbrdrt\brdrs\brdrw20\brdrcf2 \clbrdrl\brdrs\brdrw20\brdrcf2 \clbrdrb\brdrs\brdrw20\brdrcf2 \clbrdrr\brdrs\brdrw20\brdrcf2 \clpadt160 \clpadl240 \clpadb160 \clpadr240 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf2 Application & Framework\cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf2 Python, Flask, Pillow (PIL)\cell \row

\itap1\trowd \taflags0 \trgaph108\trleft-108 \trcbpat7 \tamarb640 \trbrdrl\brdrnil \trbrdrr\brdrnil 
\clvertalc \clcbpat6 \clwWidth3112\clftsWidth3 \clmart10 \clmarl10 \clmarb10 \clmarr10 \clbrdrt\brdrs\brdrw20\brdrcf2 \clbrdrl\brdrs\brdrw20\brdrcf2 \clbrdrb\brdrs\brdrw20\brdrcf2 \clbrdrr\brdrs\brdrw20\brdrcf2 \clpadt160 \clpadl240 \clpadb160 \clpadr240 \gaph\cellx4320
\clvertalc \clcbpat6 \clwWidth11080\clftsWidth3 \clmart10 \clmarl10 \clmarb10 \clmarr10 \clbrdrt\brdrs\brdrw20\brdrcf2 \clbrdrl\brdrs\brdrw20\brdrcf2 \clbrdrb\brdrs\brdrw20\brdrcf2 \clbrdrr\brdrs\brdrw20\brdrcf2 \clpadt160 \clpadl240 \clpadb160 \clpadr240 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf2 Infrastructure as Code\cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf2 AWS CloudFormation\cell \row

\itap1\trowd \taflags0 \trgaph108\trleft-108 \trcbpat7 \tamarb640 \trbrdrl\brdrnil \trbrdrt\brdrnil \trbrdrr\brdrnil 
\clvertalc \clcbpat6 \clwWidth3112\clftsWidth3 \clmart10 \clmarl10 \clmarb10 \clmarr10 \clbrdrt\brdrs\brdrw20\brdrcf2 \clbrdrl\brdrs\brdrw20\brdrcf2 \clbrdrb\brdrs\brdrw20\brdrcf2 \clbrdrr\brdrs\brdrw20\brdrcf2 \clpadt160 \clpadl240 \clpadb160 \clpadr240 \gaph\cellx4320
\clvertalc \clcbpat6 \clwWidth11080\clftsWidth3 \clmart10 \clmarl10 \clmarb10 \clmarr10 \clbrdrt\brdrs\brdrw20\brdrcf2 \clbrdrl\brdrs\brdrw20\brdrcf2 \clbrdrb\brdrs\brdrw20\brdrcf2 \clbrdrr\brdrs\brdrw20\brdrcf2 \clpadt160 \clpadl240 \clpadb160 \clpadr240 \gaph\cellx8640
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf2 Monitoring & Logging\cell 
\pard\intbl\itap1\pardeftab720\partightenfactor0
\cf2 Amazon CloudWatch\cell \lastrow\row
\pard\pardeftab720\sa160\partightenfactor0

\f0\b\fs40 \cf2 \
Project Structure\
\pard\pardeftab720\sa320\partightenfactor0

\f1\b0\fs32 \cf2 The repository is organized into distinct components, reflecting a professional microservice-oriented structure.\
\pard\pardeftab720\partightenfactor0

\fs28 \cf4 \cb5 \strokec4 .\

\f4 \'84\'a5
\f1 \uc0\u9472 \u9472  application/\
\uc0\u9474    
\f4 \'84\'a5
\f1 \uc0\u9472 \u9472  Dockerfile          # Defines the main web application container\
\uc0\u9474    
\f4 \'84\'a5
\f1 \uc0\u9472 \u9472  app.py              # The Flask web server and API logic\
\uc0\u9474    
\f4 \'84\'a5
\f1 \uc0\u9472 \u9472  buildspec.yml       # Build instructions for the CI/CD pipeline\
\uc0\u9474    
\f4 \'84\'a5
\f1 \uc0\u9472 \u9472  requirements.txt    # Python dependencies for the web app\
\uc0\u9474    \u9492 \u9472 \u9472  templates/\
\uc0\u9474        \u9492 \u9472 \u9472  index.html      # Front-end HTML template\
\uc0\u9492 \u9472 \u9472  lambda/\
    
\f4 \'84\'a5
\f1 \uc0\u9472 \u9472  lambda_function.py  # Python code for the image processing Lambda\
    
\f4 \'84\'a5
\f1 \uc0\u9472 \u9472  buildspec.yml       # Build instructions for the Lambda function\
    \uc0\u9492 \u9472 \u9472  requirements.txt    # Python dependencies for the Lambda function\
\pard\pardeftab720\partightenfactor0
\cf4 \cb1 \
\pard\pardeftab720\sa160\partightenfactor0

\f0\b\fs40 \cf2 \strokec2 Setup and Deployment\
\pard\pardeftab720\sa320\partightenfactor0

\f1\b0\fs32 \cf2 This project is fully automated via the CI/CD pipeline. The initial infrastructure setup is done once with CloudFormation, and all subsequent application deployments are handled by pushing to the 
\fs28 \cf4 \cb5 \strokec4 main
\fs32 \cf2 \cb1 \strokec2  branch on GitHub.\
\pard\pardeftab720\sa160\partightenfactor0

\f0\b \cf2 Initial Infrastructure Setup (One-Time)\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sa160\partightenfactor0
\ls2\ilvl0
\f1\b0 \cf2 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	1	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Prerequisites: AWS CLI installed and configured, Docker installed.\
\ls2\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	2	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Deploy CloudFormation Stack: Deploy the 
\fs28 \cf4 \cb5 \strokec4 infrastructure/template.yml
\fs32 \cf2 \cb1 \strokec2  file via the AWS CloudFormation console. This will create the VPC, S3 bucket, DynamoDB table, and all necessary IAM roles and security groups.\
\ls2\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	3	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Create CI/CD Pipeline: Create the AWS CodePipeline as detailed in the project documentation, connecting it to this GitHub repository and configuring the CodeBuild and deployment stages.\
\pard\pardeftab720\sa160\partightenfactor0

\f0\b \cf2 Automated Deployment (For all code changes)\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sa160\partightenfactor0
\ls3\ilvl0
\f1\b0 \cf2 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	1	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Commit and push your code changes to the 
\fs28 \cf4 \cb5 \strokec4 main
\fs32 \cf2 \cb1 \strokec2  branch of this repository.\
\ls3\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	2	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 The push will automatically trigger the CodePipeline.\
\ls3\ilvl0\kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	3	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 The pipeline will build, test, and deploy the new versions of the ECS service and Lambda function.}