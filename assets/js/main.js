// Data for dynamic content
        const projectsData = [
            {
                title: "Sales Performance Dashboard",
                description: "Interactive Power BI dashboard analyzing sales trends and performance metrics.",
                image: "https://images.unsplash.com/photo-1551288049-bebda4e38f71?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80",
                tech: ["Power BI", "SQL", "DAX"],
                githubUrl: "https://github.com/AbuHumzaKhan/sales-dashboard",
                details: "Created an interactive dashboard that increased sales insights by 35% and reduced reporting time by 50%.",
                impact: "Increased sales insights by 35% and reduced reporting time by 50% for the sales team"
            },
            {
                title: "Customer Segmentation Analysis",
                description: "Cluster analysis to identify distinct customer groups for targeted marketing.",
                image: "https://images.unsplash.com/photo-1553484771-11998c592b9c?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80",
                tech: ["Python", "Scikit-learn", "Pandas"],
                githubUrl: "https://github.com/AbuHumzaKhan/customer-segmentation",
                details: "Implemented K-means clustering to identify 5 distinct customer segments, improving marketing ROI by 22%.",
                impact: "Improved marketing ROI by 22% through targeted campaigns based on customer segments"
            },
            {
                title: "E-commerce Analytics",
                description: "Comprehensive analysis of customer behavior and purchase patterns.",
                image: "https://images.unsplash.com/photo-1556155092-490a1ba16284?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80",
                tech: ["SQL", "Python", "Tableau"],
                githubUrl: "https://github.com/AbuHumzaKhan/ecommerce-analytics",
                details: "Developed a recommendation system that increased average order value by 18%.",
                impact: "Increased average order value by 18% through personalized product recommendations"
            },
            {
                title: "COVID-19 Data Analysis",
                description: "Analysis of COVID-19 spread patterns and impact on different regions.",
                image: "https://images.unsplash.com/photo-1584036561566-baf8f5f1b144?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1332&q=80",
                tech: ["Python", "Pandas", "Matplotlib"],
                githubUrl: "https://github.com/AbuHumzaKhan/covid-analysis",
                details: "Analyzed global COVID-19 data to identify trends and create predictive models for healthcare planning.",
                impact: "Provided data-driven insights for healthcare planning during the pandemic"
            },
            {
                title: "Financial Market Prediction",
                description: "Machine learning model to predict stock market trends.",
                image: "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80",
                tech: ["Python", "TensorFlow", "LSTM"],
                githubUrl: "https://github.com/AbuHumzaKhan/stock-prediction",
                details: "Built a deep learning model with 85% accuracy in predicting stock price movements.",
                impact: "Achieved 85% accuracy in predicting stock price movements using LSTM networks"
            },
            {
                title: "Social Media Sentiment Analysis",
                description: "Real-time sentiment analysis of social media posts.",
                image: "https://images.unsplash.com/photo-1432888622747-4eb9a8f5a07a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1174&q=80",
                tech: ["Python", "NLTK", "AWS"],
                githubUrl: "https://github.com/AbuHumzaKhan/sentiment-analysis",
                details: "Developed a real-time sentiment analysis tool that processes 10,000+ posts per hour with 92% accuracy.",
                impact: "Processed 10,000+ social media posts per hour with 92% accuracy for brand monitoring"
            }
        ];

        const experienceData = [
            {
                title: "Data Analyst Intern",
                company: "Cognifyz Technologies",
                duration: "March - April 2023",
                responsibilities: [
                    "Ref. : CTI/A1/C111812",
                    "Analyzed customer data to identify trends and patterns",
                    "Built predictive models for customer behavior analysis",
                    "Collaborated with team to measure campaign effectiveness"
                ],
                certificates: [
                    {
                        title: "Cognifyz Internship Certificate",
                        issuer: "Cognifyz Technologies",
                        image: "Internship Certificates/cognifyz-certificate.png"
                    }
                ],
                achievements: [
                    "Improved data processing efficiency by 25% through optimized SQL queries",
                    "Created predictive models with 85% accuracy for customer behavior analysis"
                ]
            },
            {
                title: "Data Analyst Intern",
                company: "Zaalima",
                duration: "April - June 2023",
                responsibilities: [
                    "Emp ID: 3da45a62c278895bdb2",
                    "Designed interactive dashboards for business performance monitoring.",
                    "Applied statistical methods for actionable business insights.",
                    "Collaborated with stakeholders to deliver data-driven solutions."
                ],
                certificates: [
                    {
                        title: "Zaalima Internship Certificate",
                        issuer: "Zaalima",
                        image: "Internship Certificates/zaalima-internship.png"
                    },
                    {
                        title: "Zaalima Training Certificate",
                        issuer: "Zaalima",
                        image: "Internship Certificates/zaalima-training.png"
                    }
                ],
                achievements: [
                    "Designed 5+ interactive dashboards that reduced reporting time by 40%",
                    "Developed insights that contributed to a 15% increase in customer engagement"
                ]
            },
            {
                title: "Data Analyst Intern",
                company: "CodeTech",
                duration: "June - September 2023",
                responsibilities: [
                    "Intern ID: CT12DG2709",
                    "Developed data models to improve data accuracy by 20%",
                    "Created interactive dashboards for business metrics visualization",
                    "Performed data cleaning and validation for various datasets"
                ],
                certificates: [
                    {
                        title: "CodeTech Internship Certificate",
                        issuer: "CodeTech",
                        image: "Internship Certificates/codetech-certificate.png"
                    }
                ],
                achievements: [
                    "Improved data accuracy by 20% through advanced data modeling techniques",
                    "Automated data validation processes, saving 10+ hours per week"
                ]
            },
            {
                title: "Data Analyst Intern",
                company: "Codec Technology",
                duration: "August - Ongoing",
                responsibilities: [
                    "NCS ID: E19E86-0116588288923",
                    "Designing interactive and advanced data visualization dashboards using Power BI and Python libraries.",
                    "Conducting in-depth data analysis to generate actionable insights for business growth.",
                    "Creating automated data processing pipelines"
                ],
                certificates: [],
                achievements: [
                    "Developed automated data pipelines that reduced manual processing time by 60%",
                    "Created interactive dashboards that improved decision-making speed by 40%"
                ]
            }
        ];

        const certificatesData = [
            // IBM Certificates
            {
                title: "IBM Data Analytics",
                issuer: "IBM",
                image: "Certificate/IBM Certificates/Introduction to Data Analytics.png",
                category: "ibm",
                thumbnail: "https://images.unsplash.com/photo-1587440871875-191322ee64b0?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1171&q=80"
            },
            {
                title: "Excel Basics for Data Analysis",
                issuer: "IBM",
                image: "Certificate/IBM Certificates/Excel-1.png",
                category: "ibm",
                thumbnail: "https://images.unsplash.com/photo-1590601518932-2fd9efad6c1f?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1171&q=80"
            },
            {
                title: "MySQL with Information Technology",
                issuer: "IBM",
                image: "Certificate/IBM Certificates/MySQL with Information Technology.png",
                category: "ibm",
                thumbnail: "https://images.unsplash.com/photo-1542744173-8e7e53415bb0?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80"
            },
            {
                title: "Data Analysis and Visualization Foundation",
                issuer: "IBM",
                image: "Certificate/IBM Certificates/Data Analysis and Visualization Foundation-4cource.png",
                category: "ibm",
                thumbnail: "https://images.unsplash.com/photo-1581091226033-d5c48150dbaa?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80"
            },
            {
                title: "Python for Data Science, AI & Development",
                issuer: "IBM",
                image: "Certificate/IBM Certificates/python_ai.png",
                category: "ibm",
                thumbnail: "https://images.unsplash.com/photo-1526379879527-8559ecfcaec0?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80"
            },
            {
                title: "Data Analytics and Visualization Fundamentals",
                issuer: "IBM",
                image: "Certificate/IBM Certificates/Data Analytics and visualization Fundamentals.png",
                category: "ibm",
                thumbnail: "https://images.unsplash.com/photo-1543286386-713bdd548da4?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80"
            },
            
            // LinkedIn Certificates
            {
                title: "Intro to Career Skill In Data Analytics",
                issuer: "LinkedIn",
                image: "Certificate/Linkedin Certificates/linkedin_certificate_1.png",
                category: "linkedin",
                thumbnail: "https://images.unsplash.com/photo-1542744173-8e7e53415bb0?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80"
            },
            {
                title: "Learning Data Analytics: 1 Foundations",
                issuer: "LinkedIn",
                image: "Certificate/Linkedin Certificates/linkedin_certificate_2.png",
                category: "linkedin",
                thumbnail: "https://images.unsplash.com/photo-1526379879527-8559ecfcaec0?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80"
            },
            {
                title: "Learning Data Analytics Part 2: Extending and Applying Core Knowledge",
                issuer: "LinkedIn",
                image: "Certificate/Linkedin Certificates/linkedin_certificate_3.png",
                category: "linkedin",
                thumbnail: "https://images.unsplash.com/photo-1555949963-aa79dcee981c?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80"
            },
            {
                title: "Learning Excel: Data Analysis",
                issuer: "LinkedIn",
                image: "Certificate/Linkedin Certificates/Excel Linkedin-1.png",
                category: "linkedin",
                thumbnail: "https://images.unsplash.com/photo-1590601518932-2fd9efad6c1f?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1171&q=80"
            },
            {
                title: "Learning Excel: Data Analysis",
                issuer: "LinkedIn",
                image: "Certificate/Linkedin Certificates/Excel Linkedin [(NASBA]-1.png",
                category: "linkedin",
                thumbnail: "https://images.unsplash.com/photo-1590601518932-2fd9efad6c1f?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1171&q=80"
            },
            {
                title: "SQL for Data Analysis",
                issuer: "LinkedIn",
                image: "Certificate/Linkedin Certificates/SQL Linkedin-1.png",
                category: "linkedin",
                thumbnail: "https://images.unsplash.com/photo-1542744173-8e7e53415bb0?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1170&q=80"
            },
            
            // Other Certificates
            {
                title: "Advance Data Analysis Using Excel and Power BI",
                issuer: "Let's Upgrade",
                image: "Certificate/Other Certificates/Advance Data Analysis Using Excel and Power BI.png",
                category: "other",
                thumbnail: "https://images.unsplash.com/photo-1568992687947-868a62a9f521?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1332&q=80"
            },
            {
                title: "Power BI",
                issuer: "Let's Upgrade",
                image: "Certificate/Other Certificates/Power BI.png",
                category: "other",
                thumbnail: "https://images.unsplash.com/photo-1451187580459-43490279c0fa?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1172&q=80"
            },
            
            // Other Certificates
            {
                title: "Get Start with SQL Aalysis And BI on Databricks",
                issuer: "Let's Upgrade",
                image: "Certificate/Other Certificates/Get Start with SQL Aalysis And BI on Databricks.png",
                category: "other",
                thumbnail: "https://images.unsplash.com/photo-1568992688065-536aad8c12db?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1332&q=80"
            },
            {
                title: "AWS Certified Data Analytics",
                issuer: "Amazon Web Services",
                image: "Certificate/Others/aws-analytics.png",
                category: "other",
                thumbnail: "https://images.unsplash.com/photo-1451187580459-43490279c0fa?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1172&q=80"
            }
        ];

        // Forage Job Simulations Data
        const forageData = [
            {
                title: "Data Visualization: Empowering Business with Effective Insights",
                company: "Tata Consultancy Services",
                logo: "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Tata_Consultancy_Services_Logo.svg/800px-Tata_Consultancy_Services_Logo.svg.png",
                description: "Completed a simulation involving creating data visualizations for Tata Consultancy Services. Prepared questions for a meeting with client senior leadership and created visuals for data analysis to help executives with effective decision making.",
                skills: ["Data Visualization", "Power BI", "Executive Communication", "Client Consulting"],
                link: "https://www.theforage.com/simulations/tata/data-visualisation-p5xo",
                certificateImage: "Certificate/JobSimulation/forage-certificates/tata-data-visualization.png"
            },
            {
                title: "Data Analytics and Commercial Insights",
                company: "Quantium",
                logo: "https://images.crunchbase.com/image/upload/c_lpad,f_auto,q_auto:eco,dpr_1/v1397190011/hsgarqjya9nz2u2imo.png",
                description: "Focused on Data Analytics and Commercial Insights. Developed expertise in data preparation and customer analytics, utilizing transaction datasets to extract valuable insights and deliver data-driven commercial recommendations.",
                skills: ["Data Analytics", "Customer Analytics", "Commercial Insights", "Data Preparation"],
                link: "https://www.theforage.com/simulations/quantium/data-analytics-rqkb",
                certificateImage: "Certificate/JobSimulation/forage-certificates/quantium-analytics.png"
            },
            {
                title: "Power BI Data Visualization",
                company: "PwC Switzerland",
                logo: "https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/PricewaterhouseCoopers_Logo.svg/800px-PricewaterhouseCoopers_Logo.svg.png",
                description: "Strengthened Power BI skills to better understand clients and their data visualization needs. Created Power BI dashboards that effectively conveyed KPIs, showcasing ability to respond to client requests with well-designed solutions.",
                skills: ["Power BI", "Dashboard Design", "KPI Visualization", "Client Communication"],
                link: "https://www.theforage.com/simulations/pwc-ch/power-bi-cqxg",
                certificateImage: "Certificate/JobSimulation/forage-certificates/pwc-power-bi.png"
            },
            {
                title: "Data Analytics and Visualization",
                company: "Accenture North America",
                logo: "https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Accenture.svg/800px-Accenture.svg.png",
                description: "Advised a hypothetical social media client as a Data Analyst. Cleaned, modelled and analyzed 7 datasets to uncover insights into content trends to inform strategic decisions. Prepared a PowerPoint deck and video presentation to communicate key insights.",
                skills: ["Data Cleaning", "Trend Analysis", "Strategic Insights", "Client Presentation"],
                link: "https://www.theforage.com/simulations/accenture-nam/data-analytics-mmlb",
                certificateImage: "Certificate/JobSimulation/forage-certificates/accenture-analytics.png"
            },
            {
                title: "Data Analytics",
                company: "Deloitte Australia",
                logo: "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Deloitte_Logo.svg/800px-Deloitte_Logo.svg.png",
                description: "Completed a job simulation involving data analysis and forensic technology. Created a data dashboard using Tableau and used Excel to classify data and draw business conclusions.",
                skills: ["Tableau", "Data Forensics", "Excel Analysis", "Dashboard Creation"],
                link: "https://www.theforage.com/simulations/deloitte-au/data-analytics-s5zy",
                certificateImage: "Certificate/JobSimulation/forage-certificates/deloitte-analytics.png"
            }
        ];

        // All certificates combined for modal navigation
        const allCertificates = [...certificatesData];
        
        // Add experience certificates to the allCertificates array
        experienceData.forEach(exp => {
            exp.certificates.forEach(cert => {
                allCertificates.push({
                    ...cert,
                    category: "experience"
                });
            });
        });
        
        // Add forage certificates to the allCertificates array
        forageData.forEach(forage => {
            if (forage.certificateImage) {
                allCertificates.push({
                    title: forage.title,
                    issuer: forage.company,
                    image: forage.certificateImage,
                    category: "forage",
                    thumbnail: forage.logo
                });
            }
        });

        // Initialize variables
        let currentCertificateIndex = 0;
        let currentZoom = 1;
        let projectsVisible = 6; // Number of projects to show initially
        let certificatesVisible = 6; // Number of certificates to show initially

        // DOM Elements
        const hamburger = document.querySelector('.hamburger');
        const navLinks = document.querySelector('.nav-links');
        const scrollToTopBtn = document.getElementById('scrollToTop');
        const themeToggleBtn = document.getElementById('themeToggle');
        const themeIcon = themeToggleBtn.querySelector('i');
        const contactForm = document.getElementById('contactForm');
        const certificatePreview = document.getElementById('certificatePreview');
        const previewImage = document.getElementById('previewImage');
        const previewTitle = document.getElementById('previewTitle');
        const previewIssuer = document.getElementById('previewIssuer');
        const previewClose = document.getElementById('previewClose');
        const previewPrev = document.getElementById('previewPrev');
        const previewNext = document.getElementById('previewNext');
        const certificateLoading = document.getElementById('certificateLoading');
        const zoomInBtn = document.getElementById('zoomIn');
        const zoomOutBtn = document.getElementById('zoomOut');
        const downloadBtn = document.getElementById('downloadCert');
        const showMoreProjectsBtn = document.getElementById('showMoreProjects');
        const showMoreCertificatesBtn = document.getElementById('showMoreCertificates');
        const filterButtons = document.querySelectorAll('.filter-btn');
        const projectsContainer = document.getElementById('projectsContainer');
        const experienceContainer = document.getElementById('experienceContainer');
        const forageContainer = document.getElementById('forageContainer');
        const certificatesContainer = document.getElementById('certificatesContainer');
        const toast = document.getElementById('toast');
        const toastMessage = document.getElementById('toastMessage');
        const downloadResumeBtn = document.getElementById('downloadResume');

        // Initialize the page
        function init() {
            renderProjects();
            renderExperience();
            renderForageSimulations();
            renderCertificates();
            setupEventListeners();
            setupSmoothScrolling();
            setupAnimations();
        }

        // Render projects
        function renderProjects() {
            projectsContainer.innerHTML = '';
            
            projectsData.slice(0, projectsVisible).forEach((project, index) => {
                const projectCard = document.createElement('div');
                projectCard.className = 'project-card glass';
                projectCard.innerHTML = `
                    <div class="project-card-inner">
                        <div class="project-card-front">
                            <img src="${project.image}" alt="${project.title}" class="project-image">
                            <h3>${project.title}</h3>
                            <p>${project.description}</p>
                            <div class="tech-stack">
                                ${project.tech.map(tech => `<span>${tech}</span>`).join('')}
                            </div>
                            ${project.impact ? `
                            <div class="project-impact">
                                <h4>Business Impact:</h4>
                                <p>${project.impact}</p>
                            </div>
                            ` : ''}
                            <a href="#" class="btn btn-secondary view-project-btn" data-index="${index}">View Project</a>
                        </div>
                        <div class="project-card-back">
                            <h3>${project.title}</h3>
                            <p>${project.details}</p>
                            ${project.impact ? `
                            <div class="project-impact">
                                <h4>Business Impact:</h4>
                                <p>${project.impact}</p>
                            </div>
                            ` : ''}
                            <a href="${project.githubUrl}" class="btn btn-primary" target="_blank">
                                <i class="fab fa-github"></i> GitHub
                            </a>
                        </div>
                    </div>
                `;
                projectsContainer.appendChild(projectCard);
            });

            // Update show more button text
            if (projectsVisible >= projectsData.length) {
                showMoreProjectsBtn.textContent = 'No More Projects';
                showMoreProjectsBtn.style.opacity = '0.5';
                showMoreProjectsBtn.style.pointerEvents = 'none';
            } else {
                showMoreProjectsBtn.textContent = 'Show More Projects';
                showMoreProjectsBtn.style.opacity = '1';
                showMoreProjectsBtn.style.pointerEvents = 'auto';
            }
        }

        // Render experience
        function renderExperience() {
            experienceContainer.innerHTML = '';
            
            experienceData.forEach((exp, index) => {
                const experienceCard = document.createElement('div');
                experienceCard.className = 'experience-card glass';
                
                let certificatesHTML = '';
                exp.certificates.forEach((cert, certIndex) => {
                    certificatesHTML += `
                        <button class="view-certificate-btn" data-certificate="${cert.image}" data-title="${cert.title}" data-issuer="${cert.issuer}" style="margin-top: 10px;">
                            ${cert.title}
                        </button>
                    `;
                });
                
                let achievementsHTML = '';
                if (exp.achievements && exp.achievements.length > 0) {
                    achievementsHTML = `
                        <div class="experience-achievements">
                            ${exp.achievements.map(achievement => `
                                <div class="achievement-item">
                                    <div class="achievement-icon"><i class="fas fa-trophy"></i></div>
                                    <span>${achievement}</span>
                                </div>
                            `).join('')}
                        </div>
                    `;
                }

                experienceCard.innerHTML = `
                    <h3>${exp.title}</h3>
                    <h4>${exp.company}</h4>
                    <span class="duration">${exp.duration}</span>
                    <ul>
                        ${exp.responsibilities.map(resp => `<li>${resp}</li>`).join('')}
                    </ul>
                    ${achievementsHTML}
                    ${certificatesHTML}
                `;
                
                experienceContainer.appendChild(experienceCard);
            });
        }

        // Render forage simulations
        function renderForageSimulations() {
            forageContainer.innerHTML = '';
            
            forageData.forEach((simulation, index) => {
                const forageCard = document.createElement('div');
                forageCard.className = 'forage-card glass';
                forageCard.innerHTML = `
                    <div class="forage-card-header">
                        <img src="${simulation.logo}" alt="${simulation.company}" class="forage-logo">
                        <div>
                            <h3>${simulation.title}</h3>
                            <p>${simulation.company}</p>
                        </div>
                    </div>
                    <p>${simulation.description}</p>
                    <div class="forage-skills">
                        ${simulation.skills.map(skill => `<span class="forage-skill">${skill}</span>`).join('')}
                    </div>
                    <div class="forage-actions">
                        <a href="${simulation.link}" class="btn btn-primary" target="_blank">View Simulation</a>
                        ${simulation.certificateImage ? 
                            `<button class="view-certificate-btn btn btn-secondary" data-certificate="${simulation.certificateImage}" data-title="${simulation.title}" data-issuer="${simulation.company}">View Certificate</button>` : 
                            ''}
                    </div>
                `;
                forageContainer.appendChild(forageCard);
            });
        }

        // Render certificates
        function renderCertificates() {
            certificatesContainer.innerHTML = '';
            
            certificatesData.slice(0, certificatesVisible).forEach((cert, index) => {
                const certificateCard = document.createElement('div');
                certificateCard.className = 'certificate-card glass';
                certificateCard.setAttribute('data-category', cert.category);
                certificateCard.innerHTML = `
                    <img src="${cert.thumbnail}" alt="${cert.title}" class="certificate-image">
                    <h3>${cert.title}</h3>
                    <p>${cert.issuer}</p>
                    <button class="view-certificate-btn" data-certificate="${cert.image}" data-title="${cert.title}" data-issuer="${cert.issuer}">View Certificate</button>
                `;
                certificatesContainer.appendChild(certificateCard);
            });

            // Update show more button text
            if (certificatesVisible >= certificatesData.length) {
                showMoreCertificatesBtn.textContent = 'No More Certificates';
                showMoreCertificatesBtn.style.opacity = '0.5';
                showMoreCertificatesBtn.style.pointerEvents = 'none';
            } else {
                showMoreCertificatesBtn.textContent = 'Show More Certificates';
                showMoreCertificatesBtn.style.opacity = '1';
                showMoreCertificatesBtn.style.pointerEvents = 'auto';
            }
        }

        // Setup event listeners
        function setupEventListeners() {
            // Toggle mobile navigation
            hamburger.addEventListener('click', () => {
                navLinks.classList.toggle('active');
                hamburger.innerHTML = navLinks.classList.contains('active') ? 
                    '<i class="fas fa-times"></i>' : '<i class="fas fa-bars"></i>';
            });
            
            // Close mobile nav when clicking a link
            document.querySelectorAll('.nav-links a').forEach(link => {
                link.addEventListener('click', () => {
                    navLinks.classList.remove('active');
                    hamburger.innerHTML = '<i class="fas fa-bars"></i>';
                });
            });
            
            // Scroll to top functionality
            window.addEventListener('scroll', () => {
                if (window.pageYOffset > 300) {
                    scrollToTopBtn.classList.add('active');
                } else {
                    scrollToTopBtn.classList.remove('active');
                }
            });
            
            scrollToTopBtn.addEventListener('click', () => {
                window.scrollTo({
                    top: 0,
                    behavior: 'smooth'
                });
            });

            // Theme toggle functionality
            themeToggleBtn.addEventListener('click', toggleTheme);

            // Form submission handling
            contactForm.addEventListener('submit', handleFormSubmit);

            // Show more projects
            showMoreProjectsBtn.addEventListener('click', (e) => {
                e.preventDefault();
                projectsVisible += 3;
                renderProjects();
            });

            // Show more certificates
            showMoreCertificatesBtn.addEventListener('click', (e) => {
                e.preventDefault();
                certificatesVisible += 6;
                renderCertificates();
            });

            // Certificate filtering
            filterButtons.forEach(button => {
                button.addEventListener('click', () => {
                    // Remove active class from all buttons
                    filterButtons.forEach(btn => btn.classList.remove('active'));
                    
                    // Add active class to clicked button
                    button.classList.add('active');
                    
                    const filter = button.getAttribute('data-filter');
                    
                    // Show all certificates if filter is 'all'
                    if (filter === 'all') {
                        document.querySelectorAll('.certificate-card').forEach(card => {
                            card.style.display = 'flex';
                        });
                    } else {
                        // Hide all certificates first
                        document.querySelectorAll('.certificate-card').forEach(card => {
                            card.style.display = 'none';
                        });
                        
                        // Show certificates with matching category
                        document.querySelectorAll(`.certificate-card[data-category="${filter}"]`).forEach(card => {
                            card.style.display = 'flex';
                        });
                    }
                });
            });

            // Certificate preview functionality
            document.addEventListener('click', function(e) {
                if (e.target.classList.contains('view-certificate-btn')) {
                    const certificateImage = e.target.getAttribute('data-certificate');
                    const certificateTitle = e.target.getAttribute('data-title');
                    const certificateIssuer = e.target.getAttribute('data-issuer');
                    
                    // Create a temporary certificate object
                    const certificate = {
                        title: certificateTitle,
                        issuer: certificateIssuer,
                        image: certificateImage
                    };
                    
                    // Find the index of this certificate
                    let certIndex = allCertificates.findIndex(cert => cert.image === certificateImage);
                    if (certIndex === -1) certIndex = 0;
                    
                    openCertificatePreview(certificate, certIndex);
                }
            });

            // Close preview
            previewClose.addEventListener('click', closeCertificatePreview);
            
            // Navigate to previous certificate
            previewPrev.addEventListener('click', showPrevCertificate);
            
            // Navigate to next certificate
            previewNext.addEventListener('click', showNextCertificate);
            
            // Zoom functionality
            zoomInBtn.addEventListener('click', zoomIn);
            
            zoomOutBtn.addEventListener('click', zoomOut);
            
            // Download functionality
            downloadBtn.addEventListener('click', downloadCertificate);
            
            // Close preview when clicking outside
            certificatePreview.addEventListener('click', (e) => {
                if (e.target === certificatePreview) {
                    closeCertificatePreview();
                }
            });

            // Close preview with Escape key
            document.addEventListener('keydown', handleKeydown);

            // Download resume
            downloadResumeBtn.addEventListener('click', (e) => {
                e.preventDefault();
                // This would normally trigger a download
                showToast('Resume download started!');
            });
        }

        // Setup smooth scrolling
        function setupSmoothScrolling() {
            document.querySelectorAll('a[href^="#"]').forEach(anchor => {
                anchor.addEventListener('click', function (e) {
                    e.preventDefault();
                    
                    const targetId = this.getAttribute('href');
                    if (targetId === '#') return;
                    
                    const targetElement = document.querySelector(targetId);
                    if (targetElement) {
                        targetElement.scrollIntoView({
                            behavior: 'smooth',
                            block: 'start'
                        });
                    }
                });
            });
        }

        // Setup animations
        function setupAnimations() {
            const revealElements = document.querySelectorAll('.skill-card, .timeline-item, .project-card, .experience-card, .certificate-card, .forage-card');
            
            function revealOnScroll() {
                const windowHeight = window.innerHeight;
                
                revealElements.forEach(element => {
                    const elementTop = element.getBoundingClientRect().top;
                    
                    if (elementTop < windowHeight - 100) {
                        element.style.animation = 'fadeIn 1s ease forwards';
                    }
                });
            }
            
            window.addEventListener('scroll', revealOnScroll);
            window.addEventListener('load', revealOnScroll);
            
            // Initialize tilt effect on cards
            const tiltCards = document.querySelectorAll('.skill-card, .project-card, .experience-card, .certificate-card, .forage-card');
            
            tiltCards.forEach(card => {
                card.addEventListener('mousemove', (e) => {
                    const cardRect = card.getBoundingClientRect();
                    const x = e.clientX - cardRect.left;
                    const y = e.clientY - cardRect.top;
                    
                    const centerX = cardRect.width / 2;
                    const centerY = cardRect.height / 2;
                    
                    const rotateX = (y - centerY) / 10;
                    const rotateY = (centerX - x) / 10;
                    
                    card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateZ(10px)`;
                });
                
                card.addEventListener('mouseleave', () => {
                    card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) translateZ(0)';
                });
            });

            // Animated counter for GitHub stats
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        animateValue(document.getElementById('repoCount'), 0, 24, 2000);
                        animateValue(document.getElementById('starCount'), 0, 127, 2000);
                        animateValue(document.getElementById('forkCount'), 0, 58, 2000);
                        observer.unobserve(entry.target);
                    }
                });
            }, { threshold: 0.5 });

            observer.observe(document.querySelector('.github-section'));
        }

        // Toggle theme
        function toggleTheme() {
            const isDarkMode = document.body.getAttribute('data-theme') !== 'light';
            
            if (isDarkMode) {
                // Switch to light mode
                document.body.setAttribute('data-theme', 'light');
                document.documentElement.style.setProperty('--primary-black', '#f0f0f0');
                document.documentElement.style.setProperty('--dark-black', '#ffffff');
                document.documentElement.style.setProperty('--light-black', '#e0e0e0');
                document.documentElement.style.setProperty('--text-white', '#333333');
                document.documentElement.style.setProperty('--text-gray', '#666666');
                document.documentElement.style.setProperty('--glass-bg', 'rgba(0, 0, 0, 0.05)');
                themeIcon.classList.remove('fa-moon');
                themeIcon.classList.add('fa-sun');
            } else {
                // Switch to dark mode
                document.body.removeAttribute('data-theme');
                document.documentElement.style.setProperty('--primary-black', '#0a0a0a');
                document.documentElement.style.setProperty('--dark-black', '#000000');
                document.documentElement.style.setProperty('--light-black', '#1a1a1a');
                document.documentElement.style.setProperty('--text-white', '#ffffff');
                document.documentElement.style.setProperty('--text-gray', '#cccccc');
                document.documentElement.style.setProperty('--glass-bg', 'rgba(255, 255, 255, 0.05)');
                themeIcon.classList.remove('fa-sun');
                themeIcon.classList.add('fa-moon');
            }
        }

        // Handle form submission
        function handleFormSubmit(e) {
            e.preventDefault();
            
            // Get form values
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const message = document.getElementById('message').value;
            
            // Simple validation
            if (name && email && message) {
                // This static site has no message backend. Open the visitor's email client instead.
                const subject = encodeURIComponent(`Portfolio contact from ${name}`);
                const body = encodeURIComponent(`Name: ${name}\nEmail: ${email}\n\n${message}`);
                showToast('Opening your email app to send this message.');
                window.location.href = `mailto:abuhumzakhan87@gmail.com?subject=${subject}&body=${body}`;
            } else {
                showToast('Please fill in all fields.');
            }
        }

        // Open certificate preview
        function openCertificatePreview(certificate, index) {
            certificateLoading.style.display = 'flex';
            previewImage.style.display = 'none';
            
            previewTitle.textContent = certificate.title;
            previewIssuer.textContent = certificate.issuer;
            currentCertificateIndex = index;
            currentZoom = 1;
            previewImage.style.transform = `scale(${currentZoom})`;
            
            // Load image
            const img = new Image();
            img.onload = function() {
                previewImage.src = certificate.image;
                previewImage.style.display = 'block';
                certificateLoading.style.display = 'none';
            };
            img.onerror = function() {
                certificateLoading.innerHTML = '<i class="fas fa-exclamation-circle"></i> Error loading certificate';
                setTimeout(() => {
                    certificateLoading.style.display = 'none';
                }, 2000);
            };
            img.src = certificate.image;
            
            certificatePreview.classList.add('active');
            document.body.style.overflow = 'hidden';
        }

        // Close certificate preview
        function closeCertificatePreview() {
            certificatePreview.classList.remove('active');
            document.body.style.overflow = 'auto';
        }

        // Show previous certificate
        function showPrevCertificate() {
            currentCertificateIndex = (currentCertificateIndex - 1 + allCertificates.length) % allCertificates.length;
            const certificate = allCertificates[currentCertificateIndex];
            openCertificatePreview(certificate, currentCertificateIndex);
        }

        // Show next certificate
        function showNextCertificate() {
            currentCertificateIndex = (currentCertificateIndex + 1) % allCertificates.length;
            const certificate = allCertificates[currentCertificateIndex];
            openCertificatePreview(certificate, currentCertificateIndex);
        }

        // Zoom in
        function zoomIn() {
            if (currentZoom < 3) {
                currentZoom += 0.2;
                previewImage.style.transform = `scale(${currentZoom})`;
            }
        }

        // Zoom out
        function zoomOut() {
            if (currentZoom > 0.6) {
                currentZoom -= 0.2;
                previewImage.style.transform = `scale(${currentZoom})`;
            }
        }

        // Download certificate
        function downloadCertificate() {
            const certificate = allCertificates[currentCertificateIndex];
            const link = document.createElement('a');
            link.href = certificate.image;
            link.download = `${certificate.title.replace(/\s+/g, '_')}.png`;
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        }

        // Handle keyboard events
        function handleKeydown(e) {
            if (e.key === 'Escape' && certificatePreview.classList.contains('active')) {
                closeCertificatePreview();
            }
            
            // Navigation with arrow keys
            if (certificatePreview.classList.contains('active')) {
                if (e.key === 'ArrowLeft') {
                    showPrevCertificate();
                } else if (e.key === 'ArrowRight') {
                    showNextCertificate();
                }
            }
        }

        // Show toast notification
        function showToast(message) {
            toastMessage.textContent = message;
            toast.classList.add('show');
            
            setTimeout(() => {
                toast.classList.remove('show');
            }, 3000);
        }

        // Animate value counter
        function animateValue(element, start, end, duration) {
            let startTimestamp = null;
            const step = (timestamp) => {
                if (!startTimestamp) startTimestamp = timestamp;
                const progress = Math.min((timestamp - startTimestamp) / duration, 1);
                element.innerHTML = Math.floor(progress * (end - start) + start);
                if (progress < 1) {
                    window.requestAnimationFrame(step);
                }
            };
            window.requestAnimationFrame(step);
        }

        // Initialize the page
        init();
