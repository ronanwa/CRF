// Ronan Wallace
// 07/25/19
// ClassroomFinder Project (Java)

import org.jsoup.*;
import org.jsoup.nodes.Document;
import java.io.IOException;

public class Main {

        public static void main(String args[]){
                String url = "https://www.macalester.edu/registrar/schedules/2019fall/class-schedule/";
                Storage storage = new Storage();
                String data = getData(url);
                createCourseObject(data,storage);
                System.out.println(" ");
                System.out.println();
        }

        public static String getData(String url) {
                String data = "";
                int numberOfClasses = 0;
                try {
                        //Connect to the website
                        Document doc = Jsoup.connect(url).get();
                        System.out.println(doc);
// Gets number of offered courses for the semester
//                        Elements tdData = doc.getElementsByTag("td");
//                        for (Element td : tdData){
//                                numberOfClasses++;
//                        }
//                        System.out.println(numberOfClasses/6);
                        data = doc.select("td").text();
                        System.out.println(data);
                } catch (IOException e) {
                        e.printStackTrace();
                }
                return data;
        }

        public static void createCourseObject(String data, Storage storage){
                int index = 0;

                while (index < data.length()){

                        // 1: GRAB CODE
                        String code;
                        if (data.substring(index+10,index+11).equals(" ")) {
                                code = data.substring(index, index + 10);
                                index += 11;
                        } else if (data.substring(index+8,index+9).equals(" ")){
                                code = data.substring(index,index+8);
                                index+=9;
                        } else {
                                code = data.substring(index, index+11);
                                index += 12;
                        }

                        // 2: GRAB TITLE
                        String title = "";
                        Boolean knob = true;
                        while (knob == true){
                                if(data.substring(index, index + 5).equals("Days:")){
                                        knob = false;
                                        index+=6;
                                        break;
                                } else {
                                        title+=data.substring(index, index+1);
                                        index++;
                                }
                        }

                        // 3: GRAB DAY
                        String day = "";
                        Boolean knob2 = true;
                        while (knob2 == true){
                                if(data.substring(index, index + 5).equals("Time:")){
                                        knob2 = false;
                                        index+=6;
                                        break;
                                } else {
                                        day+=data.substring(index, index+1);
                                        index++;
                                }
                        }

                        // 4: GRAB TIME
                        String time = "";
                        Boolean knob3 = true;
                        while (knob3 == true){
                                if(data.substring(index, index + 5).equals("Room:")){
                                        knob3 = false;
                                        index+=6;
                                        break;
                                } else {
                                        time+=data.substring(index, index+1);
                                        index++;
                                }
                        }

                        // 5: GRAB ROOM
                        String room = "";
                        Boolean knob4 = true;
                        while (knob4 == true){
                                if(data.substring(index, index + 11).equals("Instructor:")){
                                        knob4 = false;
                                        index+=12;
                                        break;
                                } else {
                                        room+=data.substring(index, index+1);
                                        index++;
                                }
                        }

                        // 6: GRAB INSTRUCTOR
                        String instructor = "";
                        Boolean knob5 = true;
                        while (knob5 == true){
                                if(data.substring(index, index + 6).equals("Avail.")){
                                        knob5 = false;
                                        break;
                                } else {
                                        instructor+=data.substring(index, index+1);
                                        index++;
                                }
                        }

                        // 7: CREATE COURSE OBJECT
                        CourseInfo course = new CourseInfo(code,title,day,time,room,instructor);

                        // 8: STORE COURSE OBJECT
                        storeCourse(course, storage);
                        // TEST STORAGE + CLASSINFO OBJECTS
//                        System.out.println("---------- "+storage.get(course).getCode()+" ------------------------");
//                        System.out.println("Course Title: "+storage.get(course).getTitle());
//                        System.out.println("Day(s): "+storage.get(course).getDay());
//                        System.out.println("Time: "+storage.get(course).getTime());
//                        System.out.println("Room: "+storage.get(course).getRoom());
//                        System.out.println("Instructor: "+storage.get(course).getInstructor());

                        // 9: SET NEW INDEX
                        Boolean knob6 = true;
                        while (knob6 == true){
                                if (data.substring(index, index + 7).equals("Details")){
                                        knob6 = false;
                                        index+=8;
                                        break;
                                } else {
                                        index++;
                                }
                        }
                } // END WHILE LOOP
                // COOL. NOW WHAT..?....?????
        }

        public static void storeCourse(CourseInfo course, Storage storage){
                storage.addCourse(course);
        }
}
