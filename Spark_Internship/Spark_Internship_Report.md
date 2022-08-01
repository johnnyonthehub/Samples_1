#Spark Internship Report

The Spark internship was conducted at two of Spark’s central locations.

##Airedale Street MDR

The first is the Spark NZ Mayoral Drive Exchange (MDR) at 31 Airedale Street. The first week was spent mainly at this location.  

The MDR is home to Spark’s Central Auckland data centre.  The building is therefore designed to withstand earthquakes, floods and fires. 

The 9th floor of the Airedale Street facility is also home to one of NOCs (Network Operations Centre). The other centre is located in Hamilton.

The NOC takes up around ⅔ of the 9th floor space.  It consists of The Assure team, Mobile team, the hosted service desk, internal service desk, IPTel, Mobile Site Monitoring, and Network Monitoring teams. 

###Assure Team
A service desk that provides support to internal and external customers.  Co-ordinates with other network providers to provide consistent service to businesses.

###Mobile Site Monitoring
Monitors cell towers, routers, microwave transmitters etc for faults and dispatches technicians where needed.

###WINTEL Team
Provide support for Microsoft products.

###MDM Team (Mobile Device Management)
Provide second-tier support for mobile devices issued by companies and government departments. This team is able to set permissions, disable , or configure devices remotely.  An interesting example of where the MDM had to act quickly is when Ashley Bloomfield was unable to access an important e-mail on his phone prior to a press briefing. 
This team also provides support for IOT (Internet of Things) devices.

A big takeaway from observing the NOC team and others at the MDR is that as a provider of telecommunications and networking solutions, Spark has to take a proactive approach in maintaining the security and integrity of its systems.  
As a country, we're incredibly reliant on the internet beyond simply being able to browse the web or upload to Instagram.  The failure of a major network component could have catastrophic consequences for the economy or infrastructure.  At worst, it could plunge our society into utter chaos. 

As a place to work, The Airedale Street MDR appears relaxed but productive.  It seems that if you aren't busy, you're probably not doing your job.  The most interesting team to work with here appears to be the MDM.  Observing the team has inspired me to learn more about IOT.

Staff seem to be encouraged to find their particular niche in the company.  The common career trajectory at Spark is to start off in a first-tier service desk role and move up from there.  Such roles seem to provide a general knowledge of the "moving parts" at Spark.   From there, the company is very supportive of people building their knowledge and qualifications to move into more specialized roles.  It's also a very collaborative environment.  Knowledge is freely shared by those with more experience to those with less.

##Cloud Team at Spark City, Victoria Street West

After the first week, the internship was divided between the MDR (2 days) and Spark City (3 days) each week. 

The Cloud team is made up of six IT engineers (the official title for anyone on the team).  

The objective of this team is to maintain the health of the cloud services that Spark uses as well as allocate and deploy them as effectively and efficiently as possible. 
While AWS is definitely used, the team also makes use of Azure.

During my time observing the team, Terraform was being introduced.  Terraform is an Infrastructure as Code software that allows a company to manage and configure their infrastructure through configuration files. The advantage of doing it this way is that it can be used across multiple cloud platforms, using user-friendly, human-readable code.

While I wasn't able to get a demonstration of Terraform during my time at Spark, I have been inspired to add to my skillset by putting in the time to learn it. 

Another key skill to develop for a cloud role is AWS CloudFormation, another Infrastructure as Code tool.  Both tools use YAML or JSON, easy languages to learn and use due to their high level of human-readability.

###Cloud Team Projects

Thiago, the newest IT engineer and graduate of the AWS re/Start programme demonstrated a tool he had developed for the Spark Sports Team.
The team produces a lot of video content, and with the bulk of that being from the coverage of sports events, it needs to be able to store and retrieve this data in a cost-effective and efficient way. This storage is handled via AWS S3 buckets, with most of it going into Glacier storage as it won't be needed in the very near future.  
Spark Sport schedules the use of this content in a calendar, so anything stored in Glacier can be set to be retrieved at an appropriate time in advance of its usage.

As the team in Spark Sport are not necessarily technically adept, Thiago created an interface using the utility CyberDuck. 
CyberDuck creates a user-friendly cloud-storage browser across multiple cloud platforms. Each day, the browser is available to the Sports team for 12 hours using a SSO (Single Sign-On) login.  From their, the team is easily able to upload, retrieve, and download data as needed.

The Cloud team is also behind a dashboard which provides diagnostic information on Spark Sport streaming using Lamda functions.  The idea is that it quickly analyses and addresses any streaming issues before they affect the end viewer. 

All in all, my internship at Spark was a positive experience.  I was impressed both by the company culture which supports and nurtures the career paths of staff, as well as the supportive and collaborative problem-solving approach.  Team members communicate openly with team leaders and there is no real sense of hierarchy withing teams. Nor did I encounter any "stay in your lane" attitudes.

Spark is definitely a good place to get started in an IT career and offers countless opportunities for professional development.













