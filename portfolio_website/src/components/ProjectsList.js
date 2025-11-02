import React from 'react';
import Project from './Project';
import projectsData from '../data/projectsData';
import styled from 'styled-components';

const ProjectsWrapper = styled.section`
  max-width: 900px;
  margin: 2rem auto;
  padding: 1rem;
`;

const Title = styled.h1`
  text-align: center;
  color: #282c34;
  margin-bottom: 1.5rem;
`;

/**
 * ProjectsList component renders a list of Project components
 * @returns {JSX.Element} Rendered project list
 */
function ProjectsList() {
  return (
    <ProjectsWrapper>
      <Title>My Projects</Title>
      {projectsData.map(({ id, title, description, techStack }) => (
        <Project
          key={id}
          id={id}
          title={title}
          description={description}
          techStack={techStack}
        />
      ))}
    </ProjectsWrapper>
  );
}

export default ProjectsList;
