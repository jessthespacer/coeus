/*
Search through and pick out people w certain research area 'a' chosen and language 'b'
Output person name, university, URL, faculty URL, numpubs, Research areas
*/
SELECT People.LF_Name, People.URL, People.NumbPublications, People.FacultyURL, ResearchArea.Name FROM people 
INNER JOIN ResearchArea.Name ON ResearchArea.ID=People.RA_ID WHERE RA_ID IN 
    (SELECT ResearchArea.ID FROM ResearchArea WHERE ResearchArea.SubjectID IN
        (SELECT Subject.ID FROM Subject WHERE Subject.name ='a')) 
AND University_ID in 
    (SELECT ID FROM University WHERE University.LanguageID IN
        (SELECT Language.ID FROM Language WHERE Language.name ='b')) 
