function projectsCreation(input) {
    let architect_name = input[0];
    let projectsAmount = input[1];
    let timePerProject = 3;
    let needed_time = Number(projectsAmount * timePerProject);
    console.log(`The architect ${architect_name} will need ${needed_time} hours to complete ${projectsAmount} project/s.`);
}

projectsCreation(['Anatoli', 5])
