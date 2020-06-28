/*
Search through and pick out people w certain country 'a' chosen and language 'b'

Output person name, university, URL, faculty URL, numpubs, Research areas
*/
SELECT People.LF_Name, People.URL, People.NumbPublications, People.FacultyURL, ResearchArea.Name FROM people 
INNER JOIN ResearchArea.Name ON ResearchArea.ID=People.RA_ID WHERE UniversityID IN 
    (SELECT ID FROM University WHERE University.CountryID IN
        (SELECT Country.ID FROM Country WHERE Country.name ='a')) 
AND University_ID in 
    (SELECT ID FROM University WHERE University.LanguageID IN
        (SELECT Language.ID FROM Language WHERE Language.name ='b')) 
